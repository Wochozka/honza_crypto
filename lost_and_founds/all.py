import sys
import argparse
import random
import json
def rucff(filename):
    unique_characters = set()
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                unique_characters.update(line.strip().upper())
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []
    unique_characters_list = list(unique_characters)
    return unique_characters_list
num_homophones = 3
homophones = {}
def gh():
    hcs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[{]}|;:,<.>/?'
    return ''.join(random.choices(hcs, k=1))
def generate_homophones(alphabet):
    used_homophones = []
    for char in alphabet:
        homophones[char] = []
        for _ in range(num_homophones):
            homophone = gh()
            while homophone in used_homophones:
                homophone = gh()
            used_homophones.append(homophone)
            homophones[char].append(homophone)
    whs()
def whs():
    with open(args.key, 'w') as f:
        json.dump(homophones, f, indent=4)
def lhfj(filename):
    homophones_dict = {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            homophones_dict = json.load(f)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return homophones_dict
def encrypt(message, homophones):
    encrypted_message = []
    for char in message.upper():
        if char in homophones:
            substitutes = homophones[char]
            encrypted_message.append(random.choice(substitutes))
        else:
            encrypted_message.append(char)
    return ''.join(encrypted_message)
def decrypt(encrypted_message, homophones):
    decrypted_message = []
    for char in encrypted_message:
        found = False
        for key, values in homophones.items():
            if char in values:
                decrypted_message.append(key)
                found = True
                break
        if not found:
            decrypted_message.append(char)
    return ''.join(decrypted_message)
def cmdline_args():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("filename",
                   help="File with input message")
    group1 = p.add_mutually_exclusive_group(required=True)
    group1.add_argument('-e', '--encrypt', action="store_true", help="encrypt message")
    group1.add_argument('-d', '--decrypt', action="store_true", help="decrypt message")
    p.add_argument('-g', '--generate', action='store_true',
                   help="Generate new key instead use current key file (key.json).")
    p.add_argument('-k', '--key', type=str, default='key.json',
                   help="Use other key filename instead default key.json (can be used with -d or -g).")
    p.add_argument('-o', '--output', type=str, help="Write output to file.")
    p.add_argument("-v", "--verbosity", type=int, choices=[-1, 0, 1, 2], default=0,
                   help="increase output verbosity (default: %(default)s)")
    return p.parse_args()
def read_message(filename):
    file_content = ""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            file_content = f.read().upper()  # Načtení celého obsahu souboru do řetězce
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return file_content
if __name__ == '__main__':
    if sys.version_info < (3, 5, 0):
        sys.stderr.write("You need python 3.5 or later to run this script\n")
        sys.exit(1)
    try:
        args = cmdline_args()
    except ValueError:
        print('Try ./honza.py filename.py --encrypt')
        sys.exit(1)
    if args.encrypt:
        print('Encrypting...\n')
        base_alphabet = rucff(args.filename)
        if args.generate:
            generate_homophones(base_alphabet)
        encrypted = encrypt(read_message(args.filename), lhfj(args.key)).upper()
        print(read_message(args.filename))
        print(encrypted)
        try:
            with open(args.output, 'w', encoding='utf-8') as file:
                file.write(encrypted)
        except IOError:
            print(f"File writing error. Can not write to file '{args.output}'.")
            sys.exit(1)
    else:
        print('Decrypting...\n')
        if args.generate:
            print('Invalid use of srguments.')
            sys.exit(1)
        decrypted = decrypt(read_message(args.filename), lhfj(args.key)).upper()
        print(read_message(args.filename))
        print(decrypted)