# Задача №9
# По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while
# Input: 5
# Output: 120


# n = int(input('Введите число N: '))
# i=1
# result = 1
# while i <= n:
#   result *= i
#   i += 1

# print(result)


# Задача №11
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

# n = int(input("Введите число: "))
# f_i = 2
# f_1 = 0
# f_2 = 1

# while f_2 < n:
#   f_1, f_2 = f_2, f_1 + f_2
#   f_i += 1

# if (f_2 == n):
#   print(f"Номер {f_i}")
# else:
#   print(f"Номер -1")


# Задача №13
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2


# n = int(input("Введите количество дней: "))
# count = 0
# countMax = 0

# for i in range(n):
#     x = int(input(f"Темепратура {i + 1}: "))
#     if x > 0:
#         count += 1
#         if count > countMax:
#             countMax = count
#     else:
#         count = 0

# print(f"Самая длинная оттепель: {countMax} дней.")


# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9


count_wat = int(input('--> '))
min_wat = int(input('water_1: '))
max_wat = min_wat

for i in range(count_wat - 1):
    wat = int(input(f'water_{i + 2}: '))
    if wat > max_wat:
        max_wat = wat
    elif wat < min_wat:
        min_wat = wat

print(min_wat, max_wat)