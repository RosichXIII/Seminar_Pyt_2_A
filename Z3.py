# Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
# Пример:
# - Для n = 5: сумма = 11,55

number = int(input('Введите число\n'))
list_n = []
count = 1
while number >= count:
    list_n.append(round(((1+1/count)**count), 2))
    count +=1
print('Список: ', list_n)
print('Сумма чисел списка =', sum(i for i in list_n))