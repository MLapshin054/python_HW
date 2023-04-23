# Задача №31
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1 , ..., an , ..., где a0  = 0, a1  = 1, ak  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

# def fibonacci(n):
#   if n in [0, 1]:
#     return 1
#   return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(7))


# Задача №33
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# def change_rating(input_list):
#   maxx = max(input_list)
#   minn = min(input_list)

#   for i in range(len(input_list)):
#     if input_list[i] == maxx:
#         input_list[i] = minn

#   return input_list

# list_rating = [1, 3, 3, 3, 4]
# new_list = change_rating(list_rating)
# print(new_list)

# Дополнительное решение через ввод трех функций

# def find_max(new_list):
#   max_num = new_list[0]
#   for i in new_list:
#     if i > max_num:
#       max_num = i
#   return max_num

# def find_min(new_list):
#   min_num = new_list[0]
#   for i in new_list:
#     if i < min_num:
#       min_num = i
#   return min_num

# def worst_list(new_list):
#   maxx = find_max(new_list)
#   minn = find_min(new_list)
#   for i in range(len(new_list)):
#     if new_list[i] == maxx:
#       new_list[i] = minn

# list_1 = [1, 3, 3, 3, 4]
# print(list_1)
# worst_list(list_1)
# print(list_1)


# Задача №35
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# def prostoe_proverka(num):
#   # if num in (0, 1):
#   #   return False
#   for i in range(2, (num // 2) + 1):
#     if (num % i == 0):
#       return False
#   return True

# n = int(input('Введите число: '))
# print(prostoe_proverka(n))

# def is_it_simple_or_not(number):
#   flag = 0
#   for i in range(2, number // 2 + 1):
#     if number % i == 0:
#       return 'No'
#   return 'Yes'

# print(is_it_simple_or_not(int(input('Введите число для проверки: '))))


# Задача №37
# 15 минут
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def revers_input(n):
    num = input('Введите число -> ')
    if n == 1:
        return num
    return revers_input(n - 1) + ' ' + num
  
print(revers_input(5))
