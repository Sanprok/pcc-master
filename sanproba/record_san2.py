import json


def reader_record():
    """читает данные из файла, возвращает список из файла"""
    b = []
    try:
        with open('record.json', 'r') as rec:
            a = json.load(rec)
            if a:
                for i in a:
                    b.append(i)
                    return b
            elif a == []:
                return b
            else:
                return b
    except:  # если не указана ошибка, то все ошибка обрабатываются одинаково, или ниже второй блок except
        with open('record.json', 'w') as rec:
            b = []

            return b


def input_save_record():
    a = input_record()
    save_record(a)


def input_record(read_record=reader_record()):
    with open('record.json', 'w') as rec:
        a = []
    bar = input('Введите свой рекорд: ')
    a.append(int(bar))
    return a


def save_record(read_record):
    """ записывает полученный аргумент в файл"""
    with open('record.json', 'w') as rec:
        json.dump(read_record, rec)


def print_record(read_record=reader_record()):
    """ выводит нумерованную таблицу рекордов"""
    qq = 1
    for i in read_record:
        print(str(qq) + ': - ' + str(i))
        qq += 1


def best_record(best_rec_col=5):
    b = reader_record()
    """выдает срез из лучших результатов - количество лучших результатов задается в параметре best_rec_col"""
    try:
        a = input('1 - вывести лучшие результаты\n2 - вывести худшие результаты\nВведите ваш выбор: ')
        if a == '1':
            if b == []:
                print('Список пуст полностью')
            else:
                b.sort()
                print_record(b)
        elif a == '2':
            b = read_record
            b.sort(reverse=True)
            print_record(b)
        elif a == '3':
            b = read_record[:best_rec_col]
            print_record(b)
    except:
        a = input('Список пускт. Введите первые результаты. Для продолжения нажмите клавишу любую клавишу')
        if a:
            pass


def record_sort(read_record=reader_record()):
    """ сортирует полученный в качестве аргумента список"""


def record_del(read_record=reader_record()):
    d = input('Введите номер рекорда для его удаления: ')
    del read_record[int(d)]
    save_record(read_record)


def file_none():
    try:
        file = open('record.json')
    except:
        with open('record.json', 'tw', encoding='utf-8') as f:
            pass

            # with open('record.json', 'w') as rec:
            #     a = 'san'
            #     rec.write(a)
            #     json.dump(a, rec)

            # else:
            # with file:
            #     print(u'нашли файл')


def meny():
    while True:
        a = input(
            'Выберете пункт меню:\n0 - Выйти\n1 - Показать рекорды\n2 - Добавать рекорд\n3 - Удалить рекорд\n4 - Сортировать список\nВаш выбор: ')
        if a == '0':
            break
        elif a == '1':
            best_record()
        elif a == '2':
            input_save_record()
        elif a == '3':
            record_del()
        elif a == '4':
            record_sort()


# file_none()

meny()
