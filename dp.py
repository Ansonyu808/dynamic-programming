def fib_old(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

def fib(n, mem = {}):
    if n in mem:
        return mem[n]
    if n <= 2:
        return 1
    mem[n] = fib(n-1, mem) + fib(n-2, mem)
    return mem[n]

# print('fib_old', fib_old(50))
# print('fib', fib(50))

def grid_traveler_old(m, n):
    if m == n == 2:
        return 2
    if m == 1 or n == 1:
        return 1
    return grid_traveler(m - 1, n) + grid_traveler(m, n - 1)

def grid_traveler(m, n, memo = {}):
    if (m,n) in memo:
        return memo[m,n]
    if (n,m) in memo:
        return memo[n,m]

    if m == n == 2:
        return 2
    if m == 1 or n == 1:
        return 1
    if m == 0 or n == 0:
        return 0 

    memo[m,n] = grid_traveler(m - 1, n) + grid_traveler(m, n - 1)
    return memo[m,n]

# print('grid_traveller_old', grid_traveler_old(18, 18))
# print('grid_traveller', grid_traveler(18, 18))

