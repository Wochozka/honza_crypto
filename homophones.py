#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2.5.2024
@author: Wochozka

Description: Generate homophones unit.
"""

import random
import json

# Abeceda, kterou chceme šifrovat - defaultní
default_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Počet homofonních jednotek pro každý znak abecedy
num_homophones = 3

# Slovník pro ukládání homofonních jednotek
homophones = {}


# Funkce pro generování náhodné homofonní jednotky
def generate_homophone():
    homophone_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[{]}|;:,<.>/?'
    return ''.join(random.choices(homophone_characters, k=1))


def generate_homophones(alphabet=default_alphabet):
    # Generování homofonních jednotek
    used_homophones = []  # Seznam pro záznam použitých znaků
    for char in alphabet:
        homophones[char] = []
        for _ in range(num_homophones):
            homophone = generate_homophone()
            while homophone in used_homophones:
                homophone = generate_homophone()
            used_homophones.append(homophone)
            homophones[char].append(homophone)
    write_homophones()


def write_homophones():
    # Uložení homofonních jednotek do JSON souboru
    with open('key.json', 'w') as file:
        json.dump(homophones, file, indent=4)
