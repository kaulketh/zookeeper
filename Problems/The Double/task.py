# put your python code here
from string import ascii_lowercase as alphabet

double_alphabet = {}


def build():
    for c in alphabet:
        double_alphabet[c] = c * 2


build()
