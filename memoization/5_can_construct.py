# Write a function 'can_construct(target, word_bank)' that accepts a
# target String and an array of strings

# The function should return a boolean indicating whether or not the target can be constructed
# From concatenating strings in the word_bank array

# You may reuse elements from word bank as many times as needed

from collections import defaultdict


def can_construct(target, word_bank, memo):
    if target in memo:
        return memo[target]
    if target == "":
        return True
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word) :]
            if can_construct(suffix, word_bank, memo):
                memo[target] == True
                return True
    memo[target] == False
    return False


memo = defaultdict(bool)
print(can_construct("abcdef", ["ab", "abc", "def", "abcd"], memo.copy()))
print(
    can_construct(
        "skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], memo.copy()
    )
)
print(
    can_construct(
        "enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], memo.copy()
    )
)
print(
    can_construct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeeeee"],
        memo.copy(),
    )
)
