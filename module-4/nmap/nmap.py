import socket
import argparse
import concurrent.futures
from typing import List

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
    # ... continue up to port 1000 as needed
}

def resolve_host_ip_from_name(host):
    try:
        ip = socket.gethostbyname(host)
        print(f"[INFO] IP address for {host} is {ip}")
        return ip
    except socket.gaierror:
        print(f"[ERROR] Could not resolve host {host}.")
        return None

def scan_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_connection:
        socket_connection.settimeout(1)
        result = socket_connection.connect_ex((ip, port))
        if result == 0:
            service_name = COMMON_PORTS.get(port, "Unknown Service") if port <= 1000 else "Unknown"
            print(f"Port {port} is open (Service: {service_name})")
            return port, True, service_name
        else:
            print(f"Port {port} is closed")
            return port, False, "Unknown"

def scan_port_range(target_ip: str, port_range: List[str]):
    open_ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        test_port = {executor.submit(scan_port, target_ip, port): port for port in port_range}
        for future in concurrent.futures.as_completed(test_port):
            port, is_open, service_name = future.result()
            if is_open:
                open_ports.append((port, service_name))
    return open_ports

def parse_port_range(port_range_str):
    min_port, max_port = port_range_str.split("-")
    try:
        if min_port == "" or max_port == "":
            raise ValueError("Invalid port values provided")
        else:
            min_port = int(min_port)
            max_port = int(max_port)
        if min_port < 1 or max_port > 65536:
            raise ValueError("Illegal value for port boundary provided")
    except ValueError:
        min_port = 0
        max_port = 65536
    finally:
        return range(min_port, max_port + 1)

def main():
    parser = argparse.ArgumentParser(description="Simple Port Scanner in Python")
    parser.add_argument("host", required=True,type=str, help="IP address or hostname of the target system")
    parser.add_argument("-p", "--ports", type=str, required=True, help="Port range (e.g., 20-80) or - for all ports")
    args = parser.parse_args()

    ip = resolve_host_ip_from_name(args.host)
    if ip is None:
        return

    port_range = parse_port_range(args.ports)
    print(f"[INFO] Scanning ports from {port_range[0]} to {port_range[-1]}")

    open_ports = scan_port_range(ip, port_range)
    if len(open_ports) > 0:
        print(f"[INFO] Open ports: {', '.join(f'{port} ({service})' for port, service in open_ports)}")
    else:
        print("[INFO] No open ports found.")

if __name__ == "__main__":
    main()
