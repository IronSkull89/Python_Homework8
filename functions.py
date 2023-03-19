from classes import Subscriber

def write_subscriber(dir_file, subscriber, separator):
    with open(dir_file, 'a', encoding='utf-8') as data:
        data.write(f'\n{subscriber_to_str(subscriber,separator)}')

def read_data(dir_file):
    with open(dir_file, 'r', encoding='utf-8') as f:
        data = list(str(f.read()).split('\n'))
    return data

def search_subscriber(book, searching_data, separator):
    result = []
    for el_str in book:
        if searching_data.lower() in el_str.lower():
            el = el_str.split(separator)
            result.append(Subscriber(book.index(el_str), el[0], el[1]))
    return result

def write_file(data, directory):
    with open(data, 'w', encoding='utf-8') as f:
        f.write('\n'.join(directory))

def subscriber_to_str(subscriber, separator):
    return subscriber.name + separator + subscriber.phone