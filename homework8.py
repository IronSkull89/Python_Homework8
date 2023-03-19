separator = " | "

class Subscriber:
    
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def update(self, name, phone):
        self.name = name
        self.phone = phone


def write_subscriber(subscriber):
    with open('data.txt', 'a', encoding='Utf-8') as data:
        data.write(f'{subscriber.name}{separator}{subscriber.phone}')


def read_data():
    with open('data.txt', 'r', encoding='Utf-8') as f:
        data = list(str(f.read()).split('\n'))
    return data


def search_subscriber(book, searching_data):
    result = []
    for el_str in book:
        if searching_data.lower() in el_str.lower():
            el = el_str.split(separator)
            result.append(Subscriber(el[0], el[1]))
    return result

def subscriber_menu():
    while True:
        print('1 - редактирование\n2 - удаление\n0 - назад')
        mode = input('Выбор режима работы: ')
        if mode == '1':
            create_data()
        elif mode == '2':
            print(search_user(read_data(), input('Введите данные для поиска: ')))
        elif mode == '0':
            break
        else:
            print('Неверное значение')
    return 1


def main_menu():
    while True:
        print('1 - запись\n2 - поиск\n0 - выход')
        mode = input('Выбор режима работы: ')
        if mode == '1':
            write_subscriber(Subscriber(input("Введиите ФИО нового абонента: "), input("Введиите телефон нового абонента: ")))
        elif mode == '2':
            directory = read_data()
            result_search = search_subscriber(directory, input('Найти: '))
            count = len(result_search)
            if count == 1:
                subscriber = result_search[0]
                print(f"{subscriber.name} | {subscriber.phone}")
                subscriber_menu()
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