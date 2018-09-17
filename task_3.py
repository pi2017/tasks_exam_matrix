"""
Task 3:
-------
Implement the application which generates all possible combinations for a given array elements

EXAMPLE:
Array: ["a", "b", "c"]
Result: [["a"], ["a","b"], ["a","b","c"], ["a","c"], ["a","c","b"], ["b"], ["b","a"], ["b","a","c"],
["b","c"], ["b","c","a"], ["c"], ["c","a"], ["c","a","b"], ["c","b"], ["c","b","a"]]
"""


def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

aa = combinations(['a','b','c'],2)

print(list(aa))