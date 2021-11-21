# Write a function 'all_construct(target, word_bank)' that accepts a
# target String and an array of strings

# The function should return a boolean indicating whether or not the target count_construct be constructed
# From concatenating strings in the word_bank array

# You may reuse elements from word bank as many times as needed


def all_construct_tab(target, word_bank):
    dp = [None for i in range(len(target) + 1)]
    dp[0] = [[]]

    for i in range(len(target) + 1):
        if dp[i] < 1:
            continue
        for word in word_bank:
            if target[i : len(word) + i] == word:
                if dp[len(word) + i] == None:
                    dp[len(word) + i] = []
                for construct in dp[i]:
                    dp[len(word) + i].append(construct + [word])
    # print(dp)
    return dp[i]


print(all_construct_tab("purple", ["purp", "p", "ur", "le", "purpl"]))
