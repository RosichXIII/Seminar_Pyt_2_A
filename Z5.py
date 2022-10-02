# Реализуйте алгоритм перемешивания списка.(Без использования библиотеки random)

import time

list_n = []
for i in range(1, 26):
    list_n.append(i)
print('До перемешивания:', list_n)
last_idx = len(list_n) - 1
while last_idx > 0:
    pseudo_rand_idx = int(str(time.time())[-4:]) % last_idx
    list_n[last_idx], list_n[pseudo_rand_idx] = list_n[pseudo_rand_idx], list_n[last_idx]
    last_idx -=1
print('После перемешивания:', list_n)