def binary_search():
    numbers = list(range(101))
    attempts = 0

    while True:
        try:
            mid = int(len(numbers) / 2)
            user_choice = input(f'Ваше число: {numbers[mid]}? ')
        except IndexError:
            print('\n- такого числа нет -')
            break

        if user_choice == '>':
            attempts += 1
            del numbers[:mid + 1]
        elif user_choice == '<':
            attempts += 1
            del numbers[mid:]
        elif user_choice == '=':
            attempts += 1
            print(f'\nВаше число: {numbers[mid]}'
                  f'\nПопыток: {attempts}')
            break

        if len(numbers) == 1:
            print(f'\nВаше число: {numbers[0]}'
                  f'\nПопыток: {attempts}')
            break


binary_search()
