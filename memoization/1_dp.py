def fib_old(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_memo(n, mem={}):
    if n in mem:
        return mem[n]
    if n <= 2:
        return 1
    mem[n] = fib_memo(n - 1, mem) + fib_memo(n - 2, mem)
    return mem[n]


def fib_tab(n):
    if n < 2:
        return n
    fib_array = [0 for _ in range(n + 1)]
    fib_array[1] = 1
    for i in range(2, n + 1):
        fib_array[i] = fib_array[i - 1] + fib_array[i - 2]
    return fib_array[n]


# print('fib_old', fib_old(50))
# print('fib_memo', fib_memo(50))
# print("fib_tab", fib_tab(50))


def grid_traveler_old(m, n):
    if m == n == 2:
        return 2
    if m == 1 or n == 1:
        return 1
    return grid_traveler_old(m - 1, n) + grid_traveler_old(m, n - 1)


def grid_traveler_memo(m, n, memo={}):
    if (m, n) in memo:
        return memo[m, n]
    if (n, m) in memo:
        return memo[n, m]

    if m == n == 2:
        return 2
    if m == 1 or n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    memo[m, n] = grid_traveler_memo(m - 1, n) + grid_traveler_memo(m, n - 1)
    return memo[m, n]


def grid_traveler_tab(m, n):
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, n + 1):
        dp[1][i] = 1
    for i in range(1, m + 1):
        dp[i][1] = 1

    for i in range(2, m + 1):
        for j in range(2, n + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

    return dp[m][n]


# print('grid_traveller_old', grid_traveler_old(18, 18))
print("grid_traveller_memo", grid_traveler_memo(18, 18))
print("grid_traveller_tab", grid_traveler_tab(18, 18))
