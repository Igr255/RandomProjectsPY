from typing import List
from itertools import cycle


def balanced_paren(parenstr: str) -> bool:
    list_of_brackets = []
    opening_brackets = {"(", "[", "{", "<"}
    closing_brackets = {")": "(", "]": "[", "}": "{", ">": "<"}

    for i in range(len(parenstr)):
        if parenstr[i] in opening_brackets:
            list_of_brackets.append(parenstr[i])
        elif parenstr[i] in closing_brackets:
            if not list_of_brackets:
                return False
            else:
                last_bracket = list_of_brackets.pop()
                if last_bracket != closing_brackets[parenstr[i]]:  # checking if the bracket has a closing pair
                    return False
    if list_of_brackets:
        return False
    return True


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