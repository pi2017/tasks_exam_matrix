"""

Task 1:
-------
Find the longest palindrome in a given string.

EXAMPLES:
INPUT: "abaccddccefe"
OUTPUT: "ccddcc"

INPUT: "HYTBCABADEFGHABCDEDCBAGHTFYW1234567887654321ZWETYGDE"
OUTPUT: 1234567887654321

"""


def sub_strings(s):
    l = len(s)

    for end in range(l, 0, -1):
        for i in range(l - end + 1):
            yield s[i: i + end]


def palindrome(s):
    return s == s[::-1]


def string_words(a):
    for i in sub_strings(a):
        if palindrome(i):
            return i


print('OUTPUT1:', string_words('abaccddccefe'))
print('OUTPUT2:', string_words('HYTBCABADEFGHABCDEDCBAGHTFYW1234567887654321ZWETYGDE'))
