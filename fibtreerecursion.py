def fib_memo(n):
    def fib_helper(n, memo):
        # If key is in memo, return value of key
        if n in memo:
            return memo[n]

        # Do work, but store the result in a local variable
        if n <= 1:
            result = n
        else:
            result = fib_helper(n - 1, memo) + fib_helper(n - 2, memo)
        memo[n] = result
        return result
    return fib_helper(n, {})


for i in range(41):
    print(i, fib_memo(i))
