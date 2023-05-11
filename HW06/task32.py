# Задача 32: Определить индексы элементов массива(списка), значения которых принадлежат заданному
# диапазону(т.е. не меньше заданного минимума и не больше заданного максимума)


import random

list_a = [random.randint(-15, 15) for _ in range(10)]
print(list_a)
min_value = -7
max_value = 7
for i in range(len(list_a)):
    if min_value < list_a[i] < max_value:
        print(i, end=' ')


# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list_1)):
#     if min_number <= list_1[i] <= max_number:
#         print(i)
