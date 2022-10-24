def factor_for(n):
    factorial = 1

    for i in range(1, n + 1):
        factorial *= i

    return factorial


def factor_while(n):
    factorial = 1

    while n > 1:
        factorial *= n
        n -= 1

    return factorial


def factor_recur(n):
    if n < 1:
        return 1
    else:
        return n * factor_recur(n - 1)


print(factor_for(6))
print(factor_while(6))
print(factor_recur(6))
