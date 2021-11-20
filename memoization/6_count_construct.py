# Write a function 'count_construct(target, word_bank)' that accepts a
# target String and an array of strings

# The function should return a boolean indicating whether or not the target count_construct be constructed
# From concatenating strings in the word_bank array

# You may reuse elements from word bank as many times as needed


def count_construct(target, word_bank, memo):
    if target in memo:
        return memo[target]
    if target == "":
        return 1

    count = 0
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word) :]
            num_construct = count_construct(suffix, word_bank, memo)
            count += num_construct
    memo[target] = count
    return count


memo = {}
print(count_construct("abcdef", ["ab", "abc", "def", "abcd"], memo.copy()))
print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"], memo.copy()))
print(
    count_construct(
        "enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], memo.copy()
    )
)
print(
    count_construct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeeeee"],
        memo.copy(),
    )
)
