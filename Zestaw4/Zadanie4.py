def fibonacci(n) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for x in range(n):
            b += a
            a = b-a
        return a

print(fibonacci(5))
