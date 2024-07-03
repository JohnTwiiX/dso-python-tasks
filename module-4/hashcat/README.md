# My `hashcat` tool

This folder contains the source code for my own implementation of the `hashcat` tool.
Hashcat can be used to TBD.

This is a lightweight implementation that covers the following features/options:

- `-m` `--mode`, Hash mode: 0 (MD5), 1 (SHA-1), 2 (SHA-256), 3 (SHA-512)
- `-a` `--attack`, Attack mode: 0 (Brute-Force), 1 (Dictionary)
- `-h` `--hash`, Target hash (required if -H is not used)
- `-H` `--hashfile`, File containing the target hash (required if -h is not used)
- `-w` `--wordlist`,Path to the wordlist file (required for Dictionary attack)
- `--help`, Show this help message and exit

## Features

- **Brute Force Attack**: Attempts all possible combinations of a specified character set within given length constraints to find the plaintext password.
- **Dictionary Attack**: Uses a provided wordlist to attempt to find the plaintext password for the target hash.
- **Multiple Hash Algorithms**: Supports MD5, SHA-1, SHA-256, and SHA-512.
- **Command-Line Interface**: Allows flexible configuration of attack parameters through command-line arguments.

## Getting started

### Prerequisites

- Python 3.6 or later

### Installation

1. Clone or download the script.
2. Ensure you have Python installed.

## Usage examples

### Brute Force Attack

To perform a brute-force attack, specify the hash algorithm, attack mode, and target hash. The example below performs a brute-force attack on an MD5 hash:

```bash
python hashcat.py -m 0 -a 0 -h 5d41402abc4b2a76b9719d911017c592
```

### Dictionary Attack

To perform a dictionary attack, provide the hash algorithm, attack mode, target hash, and path to a wordlist file:

```bash
python hashcat.py -m 1 -a 1 -h e99a18c428cb38d5f260853678922e03 -w wordlist.txt
```

### Help

To see a list of all available options, use:

```bash
python hashcat.py --help
```

## Code Breakdown

### Supported Hash Algorithmus

The script supports the following hash modes:

- `0`: MD5
- `1`: SHA-1
- `2`: SHA-256
- `3`: SHA-512

### Functions

- `hash_function(mode)`:
  - Returns the appropriate hash function from the `hashlib` library based on the specified mode.
  - Raises a `ValueError` if an unsupported mode is specified.
- `brute_force_attack(target_hash, hash_func)`:
  - Performs a brute-force attack by generating all possible passwords from a specified character set and length range, hashing them, and comparing to the target hash.
  - Parameters:
    - `target_hash`: The target hash to crack.
    - `hash_func`: The hash function to use.
  - Uses ASCII letters and digits with a password length range of 6 to 8 characters.
- `dictionary_attack(target_hash, hash_func, wordlist_path)`:
  - Performs a dictionary attack by reading passwords from a wordlist file, hashing them, and comparing to the target hash.
    - Parameters:
      - `target_hash`: The target hash to crack.
      - `hash_func`: The hash function to use.
      - `wordlist_path`: Path to the wordlist file.
- `main()`:
  - Parses command-line arguments and invokes the appropriate attack function.
  - Validates required parameters and handles errors.

### Notes

- The tool is designed to stop as soon as a valid password is found and reports the elapsed time.
- The brute-force attack function prints each password attempt, which can be useful for debugging or understanding the attack process.
- The script can read the target hash from a file if specified with the `-H` argument.
