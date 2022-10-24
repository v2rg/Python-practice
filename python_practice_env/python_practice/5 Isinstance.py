list_0 = ['1', '2', ['3', ['4', '5', ['6'], '7'], '8'], '9']


def is_inst(lst, new_list=[]):
    for i in lst:
        if isinstance(i, list):
            is_inst(i)
        else:
            new_list.append(i)

    return new_list


print(is_inst(list_0))
