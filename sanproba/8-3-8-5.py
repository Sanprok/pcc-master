def make_shhirt(text='I love Python.', size='L'):
    print('Размер данной футболки - ' + size + '. ' + text)
make_shhirt('Это самый большой размер.')
make_shhirt(text='Я не люблю', size='S')

def describe_city(city, republik='Россия'):
    print('Город ' + city + ' расположен в ' + republik)
describe_city('Москва')
describe_city('Киев', republik='Украина')
describe_city(republik='Англия', city='Лондон')


