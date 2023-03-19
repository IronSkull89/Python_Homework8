separator = " | "
dir_file = "data.txt"
class Subscriber:
    
    def __init__(self, index, name, phone):
        self.index = index
        self.name = name
        self.phone = phone

    def update(self, name, phone):
        self.name = name
        self.phone = phone


def write_subscriber(subscriber):
    with open(dir_file, 'a', encoding='utf-8') as data:
        data.write(f'{subscriber.name}{separator}{subscriber.phone}\n')

def read_data():
    with open(dir_file, 'r', encoding='utf-8') as f:
        data = list(str(f.read()).split('\n'))
    return data

def search_subscriber(book, searching_data):
    result = []
    for el_str in book:
        if searching_data.lower() in el_str.lower():
            el = el_str.split(separator)
            result.append(Subscriber(book.index(el_str), el[0], el[1]))
    return result

def write_file(data, directory):
    with open(data, 'w', encoding='utf-8') as f:
        for line in directory:
            f.write(f"{line}\n")

def subscriber_menu(directory, subscriber):
    while True:
        print('1 - редактирование\n2 - удаление\n0 - назад')
        mode = input('Выбор режима работы: ')
        if mode == '1':
            directory[subscriber.index] = subscriber.update(input("Введите ФИО абонента: "), input("Введите телефон абонента: "))
            write_file(dir_file, directory)
            print(f"{subscriber.name} | {subscriber.phone}")
        elif mode == '2':
            del directory[subscriber.index]
            write_file(dir_file, directory)
            print("Абонент удалён")
            break
        elif mode == '0':
            break
        else:
            print('Неверное значение')
    return subscriber

def main_menu():
    while True:
        print('1 - запись\n2 - поиск\n0 - выход')
        mode = input('Выбор режима работы: ')
        if mode == '1':
            write_subscriber(Subscriber(-1, input("Введите ФИО нового абонента: "), input("Введите телефон нового абонента: ")))
        elif mode == '2':
            directory = read_data()
            result_search = search_subscriber(directory, input('Найти: '))
            count = len(result_search)
            if count == 1:
                subscriber = result_search[0]
                print(f"{subscriber.name} | {subscriber.phone}")
                subscriber_menu(directory, subscriber)
            elif count > 1:
                print(f"По запросу найдено {count} абонента")
            elif count == 0:
                print(f"По запросу абонентов не найдено")    
        elif mode == '0':
            break
        else:
            print('Неверное значение')
    return 1        

main_menu()