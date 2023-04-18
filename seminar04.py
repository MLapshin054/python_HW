# Задача №25
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

testList = ('a a a b c a a d c d d').split()
print(type(testList))
slovar = {}
result = None
for i in testList:
  if i in slovar:
    print(f'{i}_{slovar[i]}')
    slovar[i] += 1
  else:
    print(f'{i}')
    slovar[i]=1
    

string = "a a a b c a a d c d d"
my_list = string.split()
my_dict = dict()

for i in range(len(my_list)):
    if my_list[i] in my_dict.keys():
        my_dict[my_list[i]] += 1
        my_list[i] = f"{my_list[i]}_{my_dict[my_list[i]]}"
    else:
        my_dict[my_list[i]] = 0

print(my_list)
    