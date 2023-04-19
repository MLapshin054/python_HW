
findNumber = int(input('Введите число: '))
nearNumber = myList[0]
for i in range(sizeList):
    if abs(myList[i] - findNumber) <= abs(nearNumber - findNumber):
        nearNumber = myList[i]
print('Число {} ближе всего к {}.'.format(findNumber, nearNumber))