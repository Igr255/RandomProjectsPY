from typing import List
from itertools import cycle

def caesar_list(word: str, key: List[int] = [1, 2, 3]) -> str:
    counter = cycle(key)
    new_word = []

    if not word:
        raise ValueError

    for letter in word:
        if letter.isupper() or not letter.isalpha() :
            raise ValueError
        ascii_sum = ord(letter) + next(counter)

        if ascii_sum > 122:
            ascii_sum = 97 + (ascii_sum - 123)
        new_word.append(chr(ascii_sum))
    return ''.join(new_word)


def caesar_varnumkey(word: str, *key: int) -> str:
    return caesar_list(word, list(key))