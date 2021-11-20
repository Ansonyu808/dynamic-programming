# Write a function `howSum(targetSum, numbers)` that takes in a targetSum and an array of numbers as arguments

# The function should return an array containing any combination of elements that add up to exactly the targetSum.  If there is no combination that adds up to the targetSum then return null
# If there are multiple combinations possible, you may return any single one

# Here I want to build on my can_sum example.
# Instead of returning true or false, we return our current array
# I think we probably need an other array to store the values at that point in time


def how_sum(target_sum, numbers, memo):
    if target_sum in memo:
        path = memo[target_sum]
        return path
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for num in numbers:
        remainder = target_sum - num
        current_path = how_sum(remainder, numbers, memo)
        if current_path != None:
            memo[target_sum] = current_path + [num]
            return memo[target_sum]

    memo[target_sum] = None
    return None


# Memo wasn't being properly cleared so that's why this is here
memo = {}
print(how_sum(7, [2, 3], memo.copy()))
print(how_sum(7, [5, 3, 4, 7], memo.copy()))
print(how_sum(7, [2, 4], memo.copy()))
print(how_sum(8, [2, 3, 5], memo.copy()))
print(how_sum(300, [7, 14], memo.copy()))
