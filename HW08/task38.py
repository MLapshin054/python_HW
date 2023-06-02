# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

FILE_PATH = r'C:\Users\MLapshin\Desktop\GB\05_Python\HW08\my_phone_book.txt'
# with open(FILE_PATH, 'w') as pb:
#   pb.write('Ivanov Ivan +734384384\n')
#   pb.write('Petrov Petr +456534524\n')
#   pb.write('Sidorov Kassir +789234523\n')
#   pb.write('Vinni Pukh +723245343\n')

file = FILE_PATH


def show_all_contact():
    with open(file, 'r+', encoding='UTF-8') as file_1:
        return file_1.read()


def add_new_contact():
    with open(file, 'a', encoding='UTF-8') as data:
        name = str(input('Введите имя: ')).capitalize()
        surname = str(input('Введите фамилию: ')).capitalize()
        phone_numb = str(input('Введите телефон: '))
        new_contact = f'{name} {surname} {phone_numb}\n'
        data.writelines(new_contact)
    return 'Новый контакт добавлен!'


def clear_all_data():
    with open(file, 'w', encoding='UTF-8') as data:
        data.write('')
        qst = str(input('Удалить данные? y/n '))
    return 'Удалено...' if qst == 'y' else 'Данные не удалены'


def find_contact():
    data_list = show_all_contact().split('\n')
    find_name = str(input('Введите данные для поиска: ')).capitalize()
    for i in data_list:
        res = i.split()
        if res[0] == find_name:
            return i
    else:
        return 'Контакт отсутствует в списке...'


def change_contact():
    data_list = show_all_contact()
    target = find_contact()
    new_data = str(input('Новый контакт: '))
    new_file = data_list.replace(target, new_data)
    with open(file, 'w', encoding='UTF-8') as file_2:
        file_2.write(new_file)
    return f'Контакт {target} был изменен на {new_data} успешно.'


def main_func():
    print('1. Показать весь справочник')
    print('2. Добавить контакт')
    print('3. Поиск контакта')
    print('4. Изменить контакт')
    print('5. Удалить контакты')
    print('6. Выход')

    while (user_action := int(input('Выберите функцию -> '))) != 6:
        match user_action:
            case 1:
                print(show_all_contact())
                main_func()
            case 2:
                add_new_contact()
                main_func()
            case 3:
                find_contact()
                main_func()
            case 4:
                change_contact()
                main_func()
            case 5:
                clear_all_data()
                main_func()
            case 6:
                break
            case _:
                print('Нет такой функции')


main_func()
