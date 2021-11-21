# Write a function `bestSum(targetSum, numbers)` that takes in a target sum array of numbers as arguments
# The function should return an array containing the shortest combination of numbers that add up exactly to targetSum


def best_sum(target_sum, numbers, memo):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    min_combo = None

    for num in numbers:
        remainder = target_sum - num
        current_path = best_sum(remainder, numbers, memo)
        if current_path != None:
            path = [num] + current_path
            if min_combo == None:
                min_combo = path
            if len(min_combo) > len(path):
                min_combo = path

    memo[target_sum] = min_combo
    return memo[target_sum]


memo = {}
print(best_sum(7, [5, 3, 4, 7], memo.copy()))
print(best_sum(8, [2, 3, 5], memo.copy()))
print(best_sum(8, [1, 4, 5], memo.copy()))
print(best_sum(100, [1, 2, 25], memo.copy()))


def best_sum_tab(target_sum, numbers):
    dp = [None for _ in range(target_sum + 1)]
    dp[0] = []

    for i in range(target_sum + 1):
        for number in numbers:
            if dp[i] == None or i + number not in range(target_sum + 1):
                continue
            one_sum = dp[i] + [number]
            if dp[i + number] == None or len(dp[i + number]) > len(one_sum):
                dp[i + number] = one_sum

    return dp[target_sum]


print(best_sum_tab(7, [5, 3, 4, 7]))
print(best_sum_tab(8, [2, 3, 5]))
print(best_sum_tab(8, [1, 4, 5]))
print(best_sum_tab(100, [1, 2, 25]))
