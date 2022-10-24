def fibo(n):
    fib1 = 0
    fib2 = 1

    for i in range(1, n + 1):
        print(fib1)
        fib1, fib2 = fib2, fib1 + fib2


def fibo_recur(n, fib1=0, fib2=1):
    if n < 1:
        return 1
    else:
        print(fib1)
        fib1, fib2 = fib2, fib1 + fib2
        return fibo_recur(n - 1, fib1, fib2)


fibo(10)
fibo_recur(10)
