"""
Version 1.0
Autor: Oleksii Savchenko
Kiev
2018
-------
Task 3:
-------
Implement the application which generates all possible combinations for a given array elements

EXAMPLE:
Array: ["a", "b", "c"]
Result: [["a"], ["a","b"], ["a","b","c"], ["a","c"], ["a","c","b"], ["b"], ["b","a"], ["b","a","c"],
["b","c"], ["b","c","a"], ["c"], ["c","a"], ["c","a","b"], ["c","b"], ["c","b","a"]]
"""

import itertools

a = ['a', 'b', 'c']
b = []
cc = list(itertools.combinations(a, 1)) + list(itertools.permutations(a, 2)) + list(itertools.permutations(a, 3))
cc.sort()
for e in cc:
    b.append(list(e))
print("OUTPUT:", b)
