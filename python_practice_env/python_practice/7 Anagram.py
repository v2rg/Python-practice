str_1 = 'earth'
str_2 = 'heart'


def anagram(str1, str2):
    return sorted(str1) == sorted(str2)


print(anagram(str_1, str_2))
