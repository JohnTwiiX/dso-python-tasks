import argparse
import hashlib
import itertools
import string

# Supported hash algorithms
hash_modes = {
    '0': 'md5',
    '1': 'sha1',
    '2': 'sha256',
    '3': 'sha512'
}

def translate_mode_to_hash_algorithm(mode):
    if mode == '0':
        return hashlib.md5
    elif mode == '1':
        return hashlib.sha1
    elif mode == '2':
        return hashlib.sha256
    elif mode == '3':
        return hashlib.sha512
    else:
        raise ValueError("Unsupported hash mode")

def brute_force_attack(target_hash:str, hash_func:function):
    """create hashed passwords for crack target password

    Args:
        target_hash (string): the hashed target password
        hash_func (func): dynamic hash function

    Returns:
        guess (string): the correct password
    """
    
    charset = string.ascii_letters + string.digits
    min_length = 6
    max_length = 8
    for length in range(min_length, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            guess = ''.join(guess)
            guess_hash = hash_func(guess.encode('utf-8')).hexdigest()
            print(guess)
            if guess_hash == target_hash:
                print(f"Password found: {guess}")
                return guess
    print("Password not found.")

def dictionary_attack(target_hash:str, hash_func:function, wordlist_path:str):
    """hash password of password list for crack target password

    Args:
        target_hash (string): the hashed target password
        hash_func (func): dynamic hash function
        wordlist_path (string): the path to the file with the word list

    Returns:
        guess (string): the correct password
    """

    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as wordlist:
        for word in wordlist:
            word = word.strip()
            print(word)
            word_hash = hash_func(word.encode('utf-8')).hexdigest()
            if word_hash == target_hash:
                print(f"Password found: {word}")
                return word
    print("Password not found.")

def main():
    parser = argparse.ArgumentParser(
        description="Hashcat-like tool in Python", 
        add_help=False, 
        epilog="Example usage: python script.py -m 0 -a 0 -h 5d41402abc4b2a76b9719d911017c592")

    parser.add_argument(
        '-m', '--mode', 
        required=True, choices=['0', '1', '2', '3'],
        help="Hash mode: 0 (MD5), 1 (SHA-1), 2 (SHA-256), 3 (SHA-512)")
    
    parser.add_argument(
        '-a', '--attack', 
        required=True, 
        choices=['0', '1'],
        help="Attack mode: 0 (Brute-Force), 1 (Dictionary)")
    
    parser.add_argument(
        '-h', '--hash', 
        help="Target hash (required if -H is not used)")
    
    parser.add_argument(
        '-H', '--hashfile', 
        help="File containing the target hash (required if -h is not used)")
    
    parser.add_argument(
        '-w', '--wordlist', 
        help="Path to the wordlist file (required for Dictionary attack)")
    
    parser.add_argument(
        '--help', 
        action='help', 
        help='Show this help message and exit')

    args = parser.parse_args()

    if not args.hash and not args.hashfile:
        parser.error("One of -h or -H must be provided.")

    if args.attack == '1' and not args.wordlist:
        parser.error("Wordlist must be provided for dictionary attack.")

    # define the target hash
    if args.hash:
        target_hash = args.hash.strip()
    else:
        with open(args.hashfile, 'r', encoding='utf-8', errors='ignore') as f:
            target_hash = f.read().strip()

    # choose the target hash
    hash_func = translate_mode_to_hash_algorithm(args.mode)

    # execute the attack
    if args.attack == '0':
        brute_force_attack(target_hash, hash_func)
    elif args.attack == '1':
        dictionary_attack(target_hash, hash_func, args.wordlist)

if __name__ == "__main__":
    main()