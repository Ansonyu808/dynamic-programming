# Given a target
# And some coins
# Please return the denomenations of coins where
# 1) we minimize the number of coins used.
# 2) with those coins, they add up to a target

# Ex:
# coins = [5, 4, 2, 1]
# target = 13
# Expected return = [5,4,4] because that is the min length


# coins = [5, 4, 2, 1]
# target = 13

# min_num_seen = float("inf")
# coins_for_min = [-1]

# # dumb solution
# def get_change(target, coins, change_set=[]):
#     global min_num_seen
#     global coins_for_min
#     if target == 0:
#         if min_num_seen > len(change_set):
#             min_num_seen = len(change_set)
#             coins_for_min = [change for change in change_set]
#             change_set = []
#         return
#     elif target < 0:
#         return
#     else:
#         for coin in coins:
#             temp_change_set = [change for change in change_set]
#             temp_change_set.append(coin)
#             get_change(target - coin, coins, temp_change_set)


# get_change(target, coins)
# print([x for x in coins_for_min])

# fibonacci : 0, 1, 1, 2, 3, 5, 8, 13, 21

# Memoization Top -> down
# Tabulation  bottom -> up


# [-1,-1,-1,-1,-1,-1,-1]
# [0,1,1,2,3,5,8]


def fib(n):
    dp = [-1 for _ in range(n + 1)]
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp)
    return dp[n]


print(fib(40))
