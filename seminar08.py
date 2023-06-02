# Задача №49
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# with open('phone_book_test.txt', 'w') as pb:
#   pb.write('Ivanov,Ivan,+123 ')
#   pb.write('\nPetrov,Petr,+456 ')
#   pb.write('\nSidorov,Sidr,+789 ')
#   pb.write('\nSid,Slava,+002 ')


def add_user():
  with open('phone_book_test.txt', 'a') as pb:
    pb.write('\n')
    pb.write(input('Введите Фамилия, Имя, Телефон - '))
    
def read_all_user():
  with open('phone_book_test.txt', 'r') as pb:
    for line in pb:
      print(line.strip())
      
def search_user():
  with open('phone_book_test.txt', 'r') as pb:
    search = input('Что ищем? - ')
    for line in pb:
      if search in line:
        print(line.strip())
      # else:
      #   print('Таких нет')

def info_func():
  print('1. Показать весь справочник ')
  print('2. Добавить пользователя ')
  print('3. Поиск пользователя ')
  print('4. Выход ')

info_func()
while (user_action := int(input('Выберите функцию, через цифру - '))) != 4:
  match user_action:
    case 1:
      read_all_user()
      info_func()
    case 2:
      add_user()
      info_func()
    case 3:
      search_user()
      info_func()
    case 4:
      break
    case _:
      print('Нет такой функции')