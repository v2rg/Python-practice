list_0 = [3, 5, 1, 7, 8, 3, 9]
list_1 = [1, 2, 3, 4, 5, 6, 7]

for v1 in list_0:
    for v2 in list_1:
        if v1 - v2 == 0:
            print(v1, v2)

print([(v1, v2) for v1 in list_0 for v2 in list_1 if v1 - v2 == 0])
