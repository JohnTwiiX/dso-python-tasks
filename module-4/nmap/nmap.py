import socket
import argparse
import concurrent.futures

# Common services for the first 100 ports
COMMON_PORTS = {
    20: "FTP data",
    21: "FTP control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    993: "IMAPS",
    995: "POP3S",
    # ... continue up to port 100 as needed
}

def resolve_host(host):
    try:
        ip = socket.gethostbyname(host)
        print(f"[INFO] IP address for {host} is {ip}")
        return ip
    except socket.gaierror:
        print(f"[ERROR] Could not resolve host {host}.")
        return None

def scan_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            service_name = COMMON_PORTS.get(port, "Unknown Service") if port <= 100 else "Unknown"
            print(f"Port {port} is open (Service: {service_name})")
            return port, True, service_name
        else:
            print(f"Port {port} is closed")
            return port, False, None

def port_scan(ip, port_range):
    open_ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        future_to_port = {executor.submit(scan_port, ip, port): port for port in port_range}
        for future in concurrent.futures.as_completed(future_to_port):
            port, is_open, service_name = future.result()
            if is_open:
                open_ports.append((port, service_name))
    return open_ports

def parse_port_range(port_range_str):
    if port_range_str == "-":
        return range(1, 65536)
    else:
        min_port, max_port = map(int, port_range_str.split("-"))
        return range(min_port, max_port + 1)

def main():
    parser = argparse.ArgumentParser(description="Simple Port Scanner in Python")
    parser.add_argument("host", type=str, help="IP address or hostname of the target system")
    parser.add_argument("-p", "--ports", type=str, required=True, help="Port range (e.g., 20-80) or - for all ports")
    args = parser.parse_args()

    ip = resolve_host(args.host)
    if ip is None:
        return

    port_range = parse_port_range(args.ports)
    print(f"[INFO] Scanning ports from {min(port_range)} to {max(port_range)}")

    open_ports = port_scan(ip, port_range)
    if open_ports:
        print(f"[INFO] Open ports: {', '.join(f'{port} ({service})' for port, service in open_ports)}")
    else:
        print("[INFO] No open ports found.")

if __name__ == "__main__":
    main()
