# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*
# 2 2
#     4


def sum(a: int, b: int):
    if b == 0:
        return a
    else:
        a += 1
        return sum(a, b - 1)

print(sum(2, 2))
