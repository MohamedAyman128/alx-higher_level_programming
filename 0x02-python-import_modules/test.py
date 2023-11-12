#!/usr/bin/python3
def print_alphabet():
    for letter in range(ord('A'), ord('Z') + 1):
        print(chr(letter), end='')
    print()
