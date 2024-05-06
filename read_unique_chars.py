#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2.5.2024
@author: Wochozka

Description: Read Unique Chracters from text file and store them in a set.
"""


def read_unique_characters_from_file(filename):
    unique_characters = set()  # Použijeme set pro ukládání jedinečných znaků

    # Načtení zprávy ze souboru
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                # Přidání jedinečných znaků do setu
                unique_characters.update(line.strip().upper())
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []

    # Převod setu na seznam (pokud potřebuješ seznam místo setu)
    unique_characters_list = list(unique_characters)

    return unique_characters_list
