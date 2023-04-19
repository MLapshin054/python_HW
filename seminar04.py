# Задача №25
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# testList = ('a a a b c a a d c d d').split()
# print(type(testList))
# slovar = {}
# result = None
# for i in testList:
#     if i in slovar:
#         print(f'{i}_{slovar[i]}')
#         slovar[i] += 1
#     else:
#         print(f'{i}')
#         slovar[i] = 1


# string = "a a a b c a a d c d d"
# my_list = string.split()
# my_dict = dict()

# for i in range(len(my_list)):
#     if my_list[i] in my_dict.keys():
#         my_dict[my_list[i]] += 1
#         my_list[i] = f"{my_list[i]}_{my_dict[my_list[i]]}"
#     else:
#         my_dict[my_list[i]] = 0

# print(*my_list)


# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13


input_text = """She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells"""

print(set(input_text.split()))
print(len(set(input_text.lower().split())))


# Задача №29
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих
# слайдах

number = int(input('Введите число: '))
maxNumber = number
while number != 0:
    number = int(input('Введите число: '))
    if number > maxNumber:
        maxNumber = number
print(f'Максимальное число: {maxNumber}!')

# С использованием моржового оператора
maxx = -1
while (number := int(input('Введите число: '))) != 0:
    if number > maxx:
        maxx = number
print('Максиммальное число -> {}'.format(maxx))
