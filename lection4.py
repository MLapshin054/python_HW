# def f(x):
#   return x*x

# a = f
# print(a(5))


# def calk1(a):
#   return a + a

# def calk2(a):
#   return a * a

# def math(op, x):
#   print(op(x))

# math(calk1, 5)


# def calk1(a, b):
#   return a + b

# def calk2(a, b):
#   return a * b

# def math(op, x, y):
#   print(op(x, y))

# math(calk2, 5, 45)


# lambda функция
# def calk2(a, b):
#   return a * b

# def math(op, x, y):
#   print(op(x, y))

# calk1 = lambda a, b: a + b

# math(calk1, 5, 45)

#Можно сразу передавать в math
# def calk2(a, b):
#   return a * b

# def math(op, x, y):
#   print(op(x, y))

# math(lambda a, b: a + b, 5, 55)


# Задача
# В списке хранятся числа. Нужно выбрать только четные числа и составить список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()

# for i in data:
#   if i % 2 == 0:
#     res.append((i, i**2))

# print(res)

# теперь решение с lambda функцией
# def select(f, col):
#   return [f(x) for x in col]

# def where(f, col):
#   return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)


#Функция map

# list_1 = [x for x in range(1, 20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

#Задача: С клавиатуры вводится некий набор чисел, в качестве разделителя используется пробел.
#Этот набор чисел будет считан в качестве строки.
#Как превратить list строк в list чисел?

# data = '15 156 96 3 5 8 52 5'
# print(data)

# data = list(map(int, data.split()))
# print(data)


#Функция filter

# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

# теперь решим задачу выше через уже изученые map и filter

# def where(f, col):
#   return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)


#Функция zip

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data)

# функция zip() пробегает по минимальному входящему набору:
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data)


#Функция enumerate

# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users))
# print(data)


#Работа с файлами

# colors = ['red', 'green', 'blue'] #наши передаваемые значения
# data = open('file.txt', 'a')      #здесь указан файл, к которому обращаемся и режим работы с ним
# data.writelines(colors)    #что пишем в файл и через какой разделитель
# data.close()

# colors = ['red', '8898', 'blue'] #изменим текст на цифры
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.close()

# with open('file.txt', 'w') as data:
#   data.write('line 1\n')
#   data.write('line 2\n')
  
# print(56)

# path = 'file.txt' #задаем переменную для обращения к файлу
# data = open(path, 'r') #режим работы с файлом, только чтение
# for line in data:
#   print(line)
# data.close


#Работа с молулем 'os'
#Работа с молулем 'shutil' по этим модулям см документацию в инете или методичку