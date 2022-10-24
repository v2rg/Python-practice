dict_1 = {'1': 1, '11': 11, '111': 111}
dict_2 = {'2': 2, '22': 22, '222': 222}


print(dict_1 | dict_2)

print({**dict_1, **dict_2})

print({k: v for d in (dict_1, dict_2) for k, v in d.items()})

dict_1.update(dict_2)
print(dict_1)
