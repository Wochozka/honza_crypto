#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2.5.2024
@author: Wochozka
"""

import read_unique_chars
import homophones
import cipher
import sys
import argparse


def cmdline_args():
    # Make parser object
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
    file_content = ""  # Inicializace prázdného řetězce pro obsah souboru

    # Načtení obsahu textového souboru
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

    # noinspection PyBroadException
    try:
        args = cmdline_args()
        # print(args)   # Pro nutnost zobrazit převzaté argunemty
    except ValueError:
        print('Try ./honza.py filename.py --encrypt')
        sys.exit(1)

    if args.encrypt:
        print('Encrypting...\n')
        base_alphabet = read_unique_chars.read_unique_characters_from_file(args.filename)
        if args.generate:
            homophones.generate_homophones(base_alphabet)
        encrypted = cipher.encrypt(read_message(args.filename), cipher.load_homophones_from_json(args.key)).upper()
        print(read_message(args.filename))
        print(encrypted)
        try:
            with open(args.output, 'w', encoding='utf-8') as file:
                file.write(encrypted)  # Zápis obsahu proměnné do souboru
        except IOError:
            print(f"File writing error. Can not write to file '{args.output}'.")
            sys.exit(1)
    else:
        print('Decrypting...\n')
        if args.generate:
            print('Invalid use of srguments. You can not create key file while decrypting.')
            sys.exit(1)
        decrypted = cipher.decrypt(read_message(args.filename), cipher.load_homophones_from_json(args.key)).upper()
        print(read_message(args.filename))
        print(decrypted)
