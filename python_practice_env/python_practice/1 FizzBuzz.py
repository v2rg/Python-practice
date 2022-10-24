print(['FizzBuzz' if x % 3 == 0 and x % 5 == 0 else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else x for x in
       range(1, 101)])

for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print(x, 'FizzBuzz')
    elif x % 3 == 0:
        print(x, 'Fizz')
    elif x % 5 == 0:
        print(x, 'Buzz')
    else:
        print(x)
