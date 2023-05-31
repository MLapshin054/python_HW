# Задача №47.
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

# Ввод:
#  values = [1, 23, 42, ‘asdfg’]
#  transformed_values = list(map(trasformation, values))
#  if values == transformed_values:
#   print(‘ok’)
#  else:
#   print(‘fail’)

# Вывод:
#  ok

# transformation = lambda x: x
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transormed_values = list(map(transformation, values))
# print(transormed_values)

# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transormed_values = list(map(lambda x: x, values))
# print(transormed_values)


# def func(item):
#   if item % 2 == 0:
#     return item**2
#   return item**3

# vals = [1, 2, 5, 6]
# func = lambda x: x**2 if x % 2 == 0 else x**3
# for item in vals:
#   print(func(item))

# if item % 2 == 0:
#   print(item**2)
# else:
#   print(item**3)

# vals = [3, 2, 5, 4]
# new = list(map(lambda x: x**2 if x % 2 == 0 else x**3, vals))
# print(new)


# Задача №49.
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*lst*b,
# где lst и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна

# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

# # методом "включения"
# vals = [1, 2, 3]
# #    что сделать   с каким эл-ом    при каком условии
# new = [item**2 for item in vals if item % 2 == 1]
# print(new)

# # и по старинке - через for
# new = []
# for item in vals:
#   if item % 2 == 1:
#     new.append(item**2)
# print(new)

# import math

# def find_farthest_orbit(list_of_orbits) -> tuple:
#     temp_list = [(0 if item[0] == item[1] else item[0] * item[1] * math.pi)
#                  for item in list_of_orbits]
#     return list_of_orbits[temp_list.index(max(temp_list))]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))


# Задача №51.
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.

# Ввод:                                    Вывод:
# values = [0, 2, 10, 6]                   same
# if same_by(lambda x: x % 2, values):
#   print(‘same’)
# else:
#   print(‘different’)

# def same_by(characteristic, objects):
#   return len(set(map(characteristic, objects))) in [0, 1]

# # если нужно включить два условия
#   # return True if len(set(map(characteristic, objects))) == 1 else (1 if len(set(map(characteristic,
#   # objects))) == 0 else False)

# # values = [0, 2, 10, 6]
# # if same_by(lambda x: x % 2, values):
# #   print('same')
# # else:
# #   print('different')
  
# #или через тернарный оператор
# values = [0, 2, 10, 6]
# print('Same' if same_by(lambda x: x % 2, values) else 'different')


# треним filter

# lst = [1, 2, 3, 4, 5, 6, 7]
# print(list(filter(lambda x: x > 2, lst)))

# треним enumerate
# for x in enumerate(lst):
#   print(x)

# треним zip
lst1 = [1, 2, 3, 4, 5, 6, 7]
lst2 = [11, 22, 33, 44, 55, 66, 77]
lst3 = [19, 28, 37, 46, 55, 64, 73]

for x in zip(lst1, lst2, lst3):
  print(x)