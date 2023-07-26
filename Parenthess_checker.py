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
