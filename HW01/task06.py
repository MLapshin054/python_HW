# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет
# с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме
# последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no


luckyTicket = str(input('Введите номер билета: '))
firstPart = int(luckyTicket[0]) + int(luckyTicket[1]) + int(luckyTicket[2])
secondPart = int(luckyTicket[3]) + int(luckyTicket[4]) + int(luckyTicket[5])
if firstPart == secondPart:
  print('{} -> {}'.format(luckyTicket, 'yes'))
else:
  print('{} -> {}'.format(luckyTicket, 'no'))