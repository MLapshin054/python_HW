# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5


import random
sizeList = int(input('Введите количество элементов списка: '))
myList = ([random.randint(1, 10) for i in range(sizeList)])
print(myList)

findNumber = int(input('Введите число: '))
nearNumber = myList[0]
for i in range(sizeList):
    if abs(myList[i] - findNumber) <= abs(nearNumber - findNumber):
        nearNumber = myList[i]
print('Число {} ближе всего к {}.'.format(findNumber, nearNumber))