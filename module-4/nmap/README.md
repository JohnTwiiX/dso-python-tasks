# Python Port Scanner

This Python script functions as a basic port scanner, similar to `nmap`, for scanning specified ports on a given host and determining if they are open or closed. For the first 100 ports, it also identifies the common services running on those ports.
This `README.md` provides a clear guide for anyone looking to understand and use your port scanner script.

## Features

- Supports scanning both IP addresses and DNS hostnames.
- Identifies open ports and, for common ports, reports the associated service.
- Utilizes concurrent scanning to improve performance.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Options](#options)
- [Common Ports](#common-ports)

## Installation

1. Ensure you have Python 3 installed. You can check your Python version by running:

    ```sh
    python3 --version
    ```

2. clone this repository.

    ```sh
    git clone git@github.com:JohnTwiiX/dso-python-tasks.git
    ```

3. Navigate to the directory containing the script.

    ```sh
    cd /path/to/script
    ```

4. No additional dependencies are required beyond Python's standard library.

## Usage

To run the port scanner, use the following command format:

```sh
python3 nmap.py <host> -p <port-range>
```

Replace `<host>` with the IP address or hostname of the target system and `<port-range>` with the range of ports you wish to scan.

## Examples

1. Scan a specific range of ports on a hostname:

    ```sh
    python3 nmap.py example.com -p 20-80
    ```

2. scan all ports on an IP address:

    ```sh
    python3 nmap.py 192.168.1.1 -p -
    ```

3. Scan a range of ports on an IP address:

    ```sh
    python3 nmap.py 10.0.0.1 -p 1000-2000
    ```

## Options

- `host`: The IP address or hostname of the target system
- `-p` or `--ports`: The range of ports to scan. Specify a range in the format `min-max` or use `-` to scan all ports (1-65535).

## Common Ports

The script identifies the following common services for ports up to 100:

- **20**: FTP data
- **21**: FTP control
- **22**: SSH
- **23**: Telnet
- **25**: SMTP
- **53**: DNS
- **80**: HTTP
- **110**: POP3
- **143**: IMAP
- **443**: HTTPS
- **993**: IMAPS
- **995**: POP3S

Services for other ports up to 100 can be added as needed.

### Key Sections Explained

- **Installation:** Instructions on how to get the script up and running on a local machine.
- **Usage:** Examples of how to use the script, including command-line syntax and example commands.
- **Options:** Details on the command-line arguments accepted by the script.
- **Common Ports:** Information about the services the script can identify for the first 100 ports.
