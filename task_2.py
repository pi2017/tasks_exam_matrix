"""
Version 1.0
Autor: Oleksii Savchenko
Kiev
2018
-------
Task 2:
-------
Implement an algorithm to print all valid (e.g., properly opened and closed)
combinations of n-pairs of parentheses.

EXAMPLE
Input: 3
Output: ((())), (()()), (())(), ()(()), ()()()
"""

from itertools import permutations


def valid(j):
    open, close = 0, 0
    for i in j:
        if i == '(':
            open += 1
        elif i == ')':
            close += 1
            if close > open:
                return False
    return True


def paren(j):
    perms = set(''.join(p) for p in permutations('(' * j + ')' * j))
    return [s for s in perms if valid(s)]


print('INPUT:', 3)
print('OUTPUT:', paren(3))

