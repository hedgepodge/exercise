########## Fibonacci using memoization ##########
def fib_memo(n, cache):
    if n < 3:
        return 1
    if n in cache:
        return cache[n]
    else:
        cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
        return cache[n]

def fib(n):
    # a dictionary to contain n-th fibonacci number
    fib_cache = {}
    return fib_memo(n, fib_cache)


# test
print(fib(10))
print(fib(50))
print(fib(100))


########## Fibonacci using tabulation ##########
def fib_tab(n):
    fib_table = [0, 1, 1]
    if n < 3:
        return 1
    
    for i in range(3,n+1):
        a = fib_table[i - 1] + fib_table[i - 2]
        fib_table.append(a)
    return fib_table[n]

# test
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))


########## Fibonacci space optimization ##########
def fib_optimized(n):
    current = 1
    previous = 0
    for i in range(1, n):
        previous, current = current, previous + current
    return current

# test
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))


########## maximizing profit using memoization ##########
def max_profit_memo(price_list, count, cache):
    if count < 2:
        cache[count] = price_list[count]
        return price_list[count]

    if count in cache:
        return cache[count]

    if count < len(price_list):
        profit = price_list[count]
    else:
        profit = 0

    for i in range(1, count // 2 + 1):
        profit = max(profit, max_profit_memo(price_list, i, cache) 
                 + max_profit_memo(price_list, count - i, cache))

    cache[count] = profit

    return profit


def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# test
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))


########## maximizing profit using tabulation ##########
def max_profit(price_list, count):
    profit_table = [0]

    for i in range(1, count + 1):
        if i < len(price_list):
            profit = price_list[i]
        else:
            profit = 0

        for j in range(1, i // 2 + 1):
            profit = max(profit, profit_table[j] + profit_table[i - j])

        profit_table.append(profit)

    return profit_table[count]

# test
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
