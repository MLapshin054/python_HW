# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


first_element = int(input('Введите первый элемент: '))
step = int(input('Введите шаг: '))
quantity = int(input('Введите количество элементов: '))

sequence = []
for i in range(1, quantity + 1):
    sequence.append(first_element + (i - 1) * step)
print(sequence)


# a1 = int(input())
# d = int(input())
# n = int(input())
# for i in range(n):
#   print(a1 + i * d)