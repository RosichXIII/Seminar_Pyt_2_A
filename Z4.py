# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

number = int(input('Введите число\n'))
mult_prod = 1
list_n = []
for i in range(-number, number+1):
    list_n.append(i)
print('Список:', list_n)
with open('file.txt', 'w+') as File:
    lines_quantity = random.randint(1, number)
    for i in range(lines_quantity+1):
        if i < lines_quantity:
            File.write(f'{str(random.randrange((number*2)+1))}\n')
        else:
            File.write(f'{str(random.randrange((number*2)+1))}')
    File.seek(0)
    for line in File:
        mult_prod *= list_n[int(line)]
print('Произведение элементов на позициях =', mult_prod)