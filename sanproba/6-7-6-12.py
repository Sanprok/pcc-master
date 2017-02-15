# homo = {
#     'name': 'San',
#     'first_name':  'Neb',
#     'age': '42',
#     'city': 'Kirow',
# }
# homo1 = {
#     'name': 'Por',
#     'first_name':  'Kan',
#     'age': '14',
#     'city': 'Lagonaki',
# }
# homo2 = {
#     'name': 'Santos',
#     'first_name':  'Nebula',
#     'age': '60',
#     'city': 'Rostov',
# }
# people = [
#     homo,
#     homo1,
#     homo2,
# ]
# for i in people:
#     print('Имя: ' + i['name'] + ' Фамилия: ' + i['first_name'] + ' Возраст: ' + i['age'] + ' город: ' + i['city'])
#
# lora = {
#     'хозяин': 'Сергей',
#     'вид животного': 'собака',
# }
# goga = {
#     'хозяин': 'Лиза',
#     'вид животного': 'кошка',
# }
# astor = {
#     'хозяин': 'Галя',
#     'вид животного': 'хомяк',
# }
# pets = [lora, goga, astor, ]
#
# for a in pets:
#     print('Хозяин: ' + a['хозяин'] + ' вид животного: ' + a['вид животного'])

# favorite_places = {
#     'Вася': ['Москва', 'Киев', 'Париж', ],
#     'Петя': ['Киров', 'Краснодар', 'Париж', ],
#     'Сережа': ['Гданьск', 'Киев', 'Лондон', ],
# }
# for iii, aaa in favorite_places.items():
#     print(iii + '-любимые города: ')
#     for i in aaa:
#         print(i)

#
# numbers = {
#     'San': 1,
#     'Vasy': 4,
#     'Piner': 10,
# }
# for number in numbers:
#     print('У ' + number + ' любимое число: ' + str(numbers[number]))
#
# numbers = {
#     'San': [1, 2, ],
#     'Vasy': [4, 5, ],
#     'Piner': [10, 12, 16, 22, ],
# }
# for number in numbers:
#     print('У ' + number + ' любимые числа: ' + str(list(numbers[number])))
#
# numbers = {
#     'San': [1, 2, ],
#     'Vasy': [4, 5, ],
#     'Piner': [10, 12, 16, 22, ],
# }
# for name, number in numbers.items():
#     print('У ' + name + ' любимые числа: ')
#     # iii = str(number)
#     for aa in number:
#         print(aa)

# Создали словарь cities в котором ключи это названия городов, а значения ключей в виде словаря с данными о городе
cities = {
    'Москва': {
    'country': 'Россия',
    'population': '1000000',
    'fact': 'столица',
},
    'Лондон': {
    'country': 'Англия',
    'population': '500000',
    'fact': 'на острове',
},
    'Париж': {
    'country': 'Франция',
    'population': '200000',
    'fact': 'красивый',
    }
}
for sites, d in cities.items():
    print(sites + ' это город, который находится в стране ' + d['country'] + '. Численность населения составляет ' +
          d['population'] + ' Интересный факт: ' + d['fact'])


