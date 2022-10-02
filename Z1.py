# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number = input('Введите натуральное число\n')
try:
    int(number)
    dict_length = int(number)
    if dict_length > 0:
        dict_n = {i:(3*i+1) for i in range(1, dict_length+1)}
        print(dict_n)
    else:
        print('Ошибка: введено не натуральное число')
except ValueError:
    print('Ошибка: введено не натуральное число')