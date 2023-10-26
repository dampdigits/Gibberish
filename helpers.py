""" Module creates random gibberish text """

import random
from string import ascii_letters

def random_string(length):
    """ Function to generate gibbersih text """
    text=""
    for _ in range(length):
        text += random.choice(ascii_letters)
    return text.lower()
