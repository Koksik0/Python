def factorial(n) -> int:
    result = 1
    for x in range(1, n + 1):
        result *= x
    return result

assert factorial(5) == 120