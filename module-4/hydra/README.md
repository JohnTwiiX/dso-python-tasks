# My `hydra` tool

This folder contains the source code for my own implementation of the `hydra` tool.
Hydra can be used to TBD.

This is a lightweight implementation that covers the following features/options:

- `-u` `--username`, Username for SSH login
- `-s` `--server`, True, help="Server IP or DNS for SSH login
- `-w` `--wordlist`, Wordlist for dictionary attack
- `--min`, Minimum length of passwords for brute force (default: 4)
- `--max`, Maximum length of passwords for brute force (default: 8)
- `-c` `--charset`, Charset for brute force attack (default: lowercase letters)

## Features

- **Brute Force Attack**: Tries all possible password combinations within a specified range of lengths and characters.
- **Dictionary Attack**: Attempts to log in using passwords from a provided wordlist.
- **Customizable Character Set and Length**: Allows for customization of the character set and password length for brute force attacks.
- **Command-Line Interface**: Easy-to-use command-line options for setting parameters.

## Getting started

### Prerequisites

- Python 3.6 or later
- `paramiko` library

To install `paramiko`, you can use `pip`:

```bash
pip install paramiko
```

### Installation

1. Clone or download the script.
2. ensure `paramiko` is installed in your Python environment.
3. Verify you have permissions to test the SSH server with username provided.

## Usage examples

### Brute Force Attack

To perfom a brute force attack, specify the username and server, along with optional parameters for character set and password length:

```bash
python hydra.py -u <username> -s <server_ip_or_dns> --min 4 --max 8 -c abc123
```

### Dictionary Attack

To perform a dictionary attack, provide the username, server, and a path to a wordlist file:

```bash
python hydra.py -u <username> -s <server_ip_or_dns> -w <path_to_wordlist>
```

### Help

To see a list of all available options, use:

```bash
python hydra.py -h
```

## Code Breakdown

### Functions

- `brute_force_ssh(username, server, charset, min_length, max_length)`:
  - Attempts to log in to the SSH server using every combination of passwords formed from the specified character set and lengths.
  - Parameters:
    - `username`: SSH username.
    - `server`: SSH server IP or DNS.
    - `charset`: Characters to use for generating passwords.
    - `min_length`: Minimum length of generated passwords.
    - `max_length`: Maximum length of generated passwords.
    - Returns the found password or `None` if unsuccessful.
- `dictionary_attack(username, server, wordlist)`:
  - Attempts to log in to the SSH server using passwords from a wordlist.
    - Parameters:
      - `username`: SSH username.
      - `server`: SSH server IP or DNS.
      - `wordlist`: Path to the wordlist file.
    - Returns the found password or `None` if unsuccessful.
- `main()`:
  - Parses command-line arguments and invokes either the brute force or dictionary attack function based on the presence of the wordlist argument.

### Notes

- The `paramiko` library is used for handling SSH connections.
- The tool is designed to stop as soon as a valid password is found.
- The script uses `argparse` for command-line argument parsing.
