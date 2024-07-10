# My `hydra` tool

This folder contains the source code for my own implementation of the `hydra` tool.
Hydra can be used to TBD.

This is a lightweight implementation that covers the following features/options:

| Tag                    | description                                                 | required |
| ---------------------- | ----------------------------------------------------------- | :------: |
| `-u` <br> `--username` | Username for SSH login                                      | x        |
| `-s` <br> `--server`   | Server IP or DNS for SSH login                              | x        |
| `-w` <br> `--wordlist` | Wordlist for dictionary attack                              |          |
| `--min`                | Minimum length of passwords for brute force (default: 4)    |          |
| `--max`                | Maximum length of passwords for brute force (default: 8)    |          |
| `-c` <br> `--charset`  | Charset for brute force attack (default: lowercase letters) |          |

## Features

- **Brute Force Attack**: Tries all possible password combinations within a specified range of lengths and characters.
- **Dictionary Attack**: Attempts to log in using passwords from a provided wordlist.
- **Customizable Character Set and Length**: Allows for customization of the character set and password length for brute force attacks.
- **Command-Line Interface**: Easy-to-use command-line options for setting parameters.

## Getting started

### Prerequisites

- Python 3.12.3
- `paramiko` 2.12 [more info](#notes)
- `argparse`

To install `paramiko`, you can use `pip`:

```bash
pip install paramiko
```

### Installation

1. clone the repository.
2. install dependencies.

## Usage examples

### Help

To see a list of all available options, use:

```bash
python hydra.py -h
```

### Brute Force Attack

To perfom a brute force attack, specify the username and server, along with optional parameters for character set and password length:

```bash
python hydra.py \
  -c <character set as string> \
  -s <IP address or DNS name> \
  -u <username> \
  --min <min length> \
  --max <max length>
```

### Dictionary Attack

To perform a dictionary attack, provide the username, server, and a path to a wordlist file:

```bash
python hydra.py \
  -s <IP address or DNS name> \
  -u <username> \
  -w  <Path to wordlist> 
```

## Code Breakdown

### Functions

#### `brute_force_ssh(username, server, charset, min_length, max_length)`

Attempts to log in to the SSH server using every combination of passwords formed from the specified character set and lengths.
Parameters:
| Parameter   | description                                                 |
| ----------- | ----------------------------------------------------------- |
| `username`  | SSH username                                                |
| `server`    | SSH server IP or DNS                                        |
| `min_length`| Minimum length of generated passwords.                      |
| `max_length`| Maximum length of generated passwords.                      |
| `charset`   | Charset for brute force attack (default: lowercase letters) |

Returns the found password or `None` if unsuccessful.

#### `dictionary_attack(username, server, wordlist)`

Attempts to log in to the SSH server using passwords from a wordlist.
Parameters:
| Parameter   | description             |
| ----------- | ----------------------- |
| `username`  | SSH username            |
| `server`    | SSH server IP or DNS    |
| `wordlist`| Path to the wordlist file.|

Returns the found password or `None` if unsuccessful.

#### `main()`

Parses command-line arguments and invokes either the brute force or dictionary attack function based on the presence of the wordlist argument.

### Notes

- The `paramiko` library is used for handling SSH connections.
