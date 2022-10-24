def abc_gen(n):
    if n < 1:
        yield ''
    else:
        for i in abc_gen(n - 1):
            yield 'a' + i
            yield 'b' + i
            yield 'c' + i


print(*abc_gen(3))
