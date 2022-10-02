# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Введите число\n'))
count = 1
mult_prod = 1
while number >= count:
    mult_prod = mult_prod * count
    print(mult_prod, end = ' ')
    count +=1