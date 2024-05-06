#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2.5.2024
@author: Wochozka
"""

import random
import json

# Abeceda a příslušné homofonní jednotky
default_homophones = {
    'A': ['@', '&', 'a'],
    'B': ['8', '%', 'b'],
    'C': ['(', 'c', ')'],
    'D': ['d', '#'],
    'E': ['3', 'e'],
    'F': ['f', '$'],
    'G': ['9', 'g'],
    'H': ['h', '^'],
    'I': ['1', 'i'],
    'J': ['j', '!'],
    'K': ['k', '*'],
    'L': ['l', '+'],
    'M': ['m', '-'],
    'N': ['n', '_'],
    'O': ['0', 'o'],
    'P': ['p', '?'],
    'Q': ['q', '/'],
    'R': ['r', '~'],
    'S': ['$', 's'],
    'T': ['7', 't'],
    'U': ['u', '['],
    'V': [']', 'v'],
    'W': ['w', '{'],
    'X': ['}', 'x'],
    'Y': ['y', ':'],
    'Z': ['z', ';'],
    ' ': [' '],  # mezera zůstane nezměněná
}


def load_homophones_from_json(filename):
    homophones_dict = {}  # Inicializace prázdného slovníku pro homofonní jednotky

    # Načtení JSON dat ze souboru
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            homophones_dict = json.load(file)
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