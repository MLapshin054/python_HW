# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random

sizeList = int(input('Введите количество элементов множества 1: '))
myList1 = set([random.randint(1, 10) for i in range(sizeList)])
print(myList1)

sizeList = int(input('Введите количество элементов множества 2: '))
myList2 = set([random.randint(1, 10) for i in range(sizeList)])
print(myList2)

newList = myList1.intersection(myList2)

newList2 = list(newList)
newList2.sort()
print(newList2)

# Эталонное решение задачи

# mol = [int(x) for x in input('Input n, m: ').split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in input('Input A: ').split()]
# k = set(a)
# for i in k:
#   set_1.add(i)
# b = [int(x) for x in input('Input B: ').split()]
# k1 = set(b)
# for i in k1:
#   set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#   print(i, end=' ')
