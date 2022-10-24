import string


def a1_20t(n):
    return {k: v * 5 if k == n else '' for k, v in zip(range(1, 21), string.ascii_lowercase)}


print(a1_20t(1))
print(a1_20t(5))
print(a1_20t(20))
print(a1_20t(21))
