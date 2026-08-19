def even_fib(limit):
    a, b = 1, 1
    total = 0
    while True:
        c = a + b
        if c > limit:
            break
        if c % 2 == 0:
            total = total + c
        a = b
        b = c
    return total

print(even_fib(4000000000))