# canSum function:
# Write a function `canSum(targetSum, numbers)` that takes in a target sum and an array of numbers as arguments.
# The function should return a boolean indicating wether or not it is possible to generate the targetSum using numbers from the array
# You may use an element of the array as many times as needed.  # You may assume that all input numbers are nonnegative.

# ex) canSum(7, [5,3,4,7]) -> true because 3 + 4 == 7 or 7 == 7
# ex) canSum(20, [8]) -> false because no combination of 8(s) adds up to 20
# ex) canSum(20, 10) -> true because 10 + 10


# Visualizing the problem:
# Guess, we can draw the callstack in a tree format.  Valid children nodes are nodes which are less than or = the current sum
# An easy way to draw this solution out might be using baseCase where target <= 0 and recursive step which subtracts from target, calling numbers that can fit
# test) canSum(7, [5,3,4,7,20])
#                       7
#              2      4       3    0              || 7-2 = 5, 7-3 = 4, 7-4 = 3
#                     3      4
# We can see here that we can take an 'or' of all the solutions.  Return false when negative, return true when 0, otherwise subtract from everything in the array

# Time complexity:
# for a given target m, and array a[n], we are looking at a callstack height of m elements, testing each n times.  Aka we are running n steps by m levels.
# So space is o(m) with m as size of target and time is o(n^m) because at every level we run n operations


def can_sum_old(target_sum, numbers):
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for num in numbers:
        new_target_sum = target_sum - num
        if can_sum(new_target_sum, numbers):
            return True

    return False


# print(can_sum_old(7, [2, 4]))
# print(can_sum_old(8, [2, 3, 5]))
# print(can_sum_old(300, [7, 14]))

# Now to memoize, folow the steps in the memoization.md file
# 1 add memo object
# check if memo contains the answer ( additional base case)
# In the recursive steps, replace returns with memo = whatever we were originally going to return
# now return the memo at that val


def can_sum(target_sum, numbers, memo):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for num in numbers:
        new_target_sum = target_sum - num
        if can_sum(new_target_sum, numbers, memo):
            memo[target_sum] = True
            return True

    memo[target_sum] = False
    return memo[target_sum]


# Time complexity after memoization:
# Now instead of computing n^m elements, we are looking at n elements for each element in m, so oour complexity is O(n*m) instead of O(n^m)

# memo = {}
# print(can_sum(7, [2, 4], memo.copy()))
# print(can_sum(8, [2, 3, 5], memo.copy()))
# print(can_sum(300, [7, 14], memo.copy()))


def can_sum_tab(target_sum, numbers):
    can_sum_array = [False for _ in range(target_sum + 1)]
    can_sum_array[0] = True

    # This is cool.  We are actually doing a true bottom up approach here
    # Previously I thought with these problems, we copy the recursive step, but that's a bit of a misnomer
    # While it is useful to helping get a solution, with these types of problems, it's probably more
    # Useful to visualize the problem from the bottom up and thereby come up with a bottom up
    # Approach as far as building the solution
    for i in range(target_sum + 1):
        for number in numbers:
            if can_sum_array[i] == False or i + number not in range(target_sum + 1):
                continue
            can_sum_array[i + number] = True

    return can_sum_array[target_sum]


print(can_sum_tab(7, [2, 4]))
print(can_sum_tab(8, [2, 3, 5]))
print(can_sum_tab(300, [7, 14]))
