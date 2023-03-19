import functions as f
from classes import Subscriber

def editing(subscriber):
    global directory
    subscriber.update(input("Введите ФИО абонента: "), input("Введите телефон абонента: "))
    directory[subscriber.index] = f.subscriber_to_str(subscriber, separator)
    directory.pop()
    f.write_file(dir_file, directory)
    print(f"{subscriber.name} | {subscriber.phone}")

def deleting(subscriber):
    global directory
    del directory[subscriber.index]
    f.write_file(dir_file, directory)
    print("Абонент удалён")

def output_result_search(result_search):
    count = len(result_search)
    if count == 1:
        subscriber = result_search[0]
        print(f"{subscriber.name} | {subscriber.phone}")
        subscriber_menu(subscriber)
    elif count > 1:
        print(f"По запросу найдено {count} абонента")
        print('\n'.join([f"{item.name} | {item.phone}" for item in result_search]))
    elif count == 0:
        print("По запросу абонентов не найдено")

def subscriber_menu(subscriber):
    while True:
        print('1 - редактирование\n2 - удаление\n0 - назад')
        mode = input('Выбор режима работы: ')
        if mode == '1':
            editing(subscriber) 
        elif mode == '2':
            deleting(subscriber) 
            break
        elif mode == '0':
            break
        else:
            print('Неверное значение')
    return subscriber

def main_menu():
    global directory
    while True:
        print('1 - запись\n2 - поиск\n0 - выход')
        mode = input('Выбор режима работы: ')
        if mode == '1':
            f.write_subscriber(dir_file, Subscriber(-1, input("Введите ФИО нового абонента: "), input("Введите телефон нового абонента: ")), separator)
        elif mode == '2':
            directory = f.read_data(dir_file)
            result_search = f.search_subscriber(directory, input('Найти: '), separator)
            output_result_search(result_search)
        elif mode == '0':
            break
        else:
            print('Неверное значение')
    return 1        

separator = " | "
dir_file = "data.txt"
directory = []

main_menu()