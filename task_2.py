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


def valid(n):
    open, close = 0, 0
    for i in n:
        if i == '(':
            open += 1
        elif i == ')':
            close += 1
            if close > open:
                return False
    return True


def paren(n):
    perms = set(''.join(p) for p in permutations('(' * n + ')' * n))
    return [s for s in perms if valid(s)]


print('INPUT:', 3)
print('OUTPUT:', paren(3))

"""def all_parens(n):
    def print_parens(left, right, s):
        if right == n:
            print(s)
            return
        if left < n:
            print_parens(left + 1, right, s + "(")
        if right < left:
            print_parens(left, right + 1, s + ")")

    print_parens(0, 0, "")

all_parens(3)
"""
