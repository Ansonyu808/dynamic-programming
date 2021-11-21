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


def can_construct_tab(target, word_bank):
    dp = [False for _ in range(len(target) + 1)]
    dp[0] = True

    for i in range(len(target) + 1):
        for word in word_bank:
            if dp[i] == False or len(word) + i > len(target) + 1:
                continue
            if target[i : len(word) + i] == word:
                dp[len(word) + i] = True
    return dp[len(target)]


print()
print()
print(can_construct_tab("abcdef", ["ab", "abc", "def", "abcd"]))
print(can_construct_tab("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(can_construct_tab("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(
    can_construct_tab(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeeeee"],
    )
)
