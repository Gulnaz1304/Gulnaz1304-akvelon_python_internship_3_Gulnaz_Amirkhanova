def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# remembers only two previous numbers


print(fibonacci(3))
