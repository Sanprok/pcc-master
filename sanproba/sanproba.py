# from builtins import print
#
# for l in list(range(1, 10)):
#     # когда пустой спискок создан в самом цикле, то каждый раз новый элемент добавляется в пустой список 13=[]
#     l3 = []
#     l3.append(l ** 2)
#     print(l3)
# # Когда пустой список создан в глобальном пространстве, то все добавленные элементы сохраняются в списке
# l3 = []
# for l in list(range(1, 10)):
#     l3.append(l ** 2)
#     print(l3)
#
# # range работает в связке с for, в этом случае list не нужен. Но если надо сохранить числа в спискок, то использовать list
# l3 = []
# for l in range(1, 10):
#     l3.append(l ** 2)
#     print(l3)
#
# # ВСе еще проще с генератором списка
# dogs = [r * 'Привет ' for r in range(1, 4)]
# print('Генератор списка в действии ', dogs)
#
# # выводит на печать не генерируемые числа а только само range(1,10)
# d = range(1, 10)
# print(d)
# print(range(1, 10))
#
# # Так правильно - выведет список из всех сгенерируемых цифр
# ll = list(range(1, 10))
# rint(ll)
#
# ddd = [1, 2, 3, 4]
# print(max(ddd))
# print(min(ddd))
# print(sum(ddd))
# ff = ['Оля', 'Света', 'Таня', 'Люба', 'Герман']
# print(ff[1])
# print(ff[2:4])
# print(ff[-3:])
# dd = ff
# dd.append('Валера')
# print(dd)
# print(ff)
#
# home = {'hair': 'black', 'glaz': 'blue'}
# print(home['hair'])
# home['rost'] = 170
# print(home)
#
# home['rost'] = 150
# print(home)
# home['rost'] += 100
# print(home)
#
# aliens = []
# # Создание 30 зеленых пришельцев.
# for alien_number in range(3):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
#
# a = ['dddkss']
# b = 'sad'
# a.append(b)
# print(a)
#
# a = ['a', 'f', 'c', ]
# print(a)
# for i in a:
#     print(i)
#

#
# noprover = ['san', 'piter', 'dido', 'master', 'lola', ]
# prover = []
# bb = len(noprover)
# cc = 0
# while cc != bb:
#     for i in noprover:
#         print('Если пользователь ' + i + ' проверен, то введите букву "y"')
#         a = input()
#         if a == 'y':
#             prover.append(i)
#         cc += 1
# print(prover)

# #  Усовершенствуем
# noprover = ['san', 'piter', 'dido', 'master', 'lola', ]
# prover = []
# while noprover:
#     for i in noprover:
#         print('Пользователь ' + i + ' проверен')
#         b = 0
#         a = noprover.pop(b)
#         prover.append(a)
#         b += 1
# print(prover)

# #  Усовершенствуем по учебнику. Повтор пока не закончится список. Каждый проход удаляем из первого списка элемент
# # и помещаем в память (pop), которую присваиваем переменной "а", затем добавляем это значение в конец нового списка
# noprover = ['san', 'piter', 'dido', 'master', 'lola', ]
# prover = []
# while noprover:
#     a = noprover.pop()
#     prover.append(a)
#     print('Пользователь ' + a + ' проверен')
#
# for i in prover:
#     print(i.title())
#
# polzov = {}
# while True:
#     # если polzov находится внутри цикла, то он каждый раз перезависывает значение переменных a и b, поэтому
#     # сохраняется всегда только последний введенный пользователь. Если вынести за пределы цикла, то цикл уже не может
#     # перезаписать данные в глобальном словаре и догда все работает, сохраняются все значения.
#     # polzov = {}    - вот так неправильно
#     a = input('Введите имя пользователя')
#     if a == '':
#         break
#     b = input('Введите любимое число')
#     polzov[a] = b
# print(polzov)

# polzov = {}
# flag = True
# while flag:
#     a = input('Введите имя пользователя')
#     b = input('Введите любимое число')
#     polzov[a] = b
#     c = input('Если не хотите продолжать, введите n:')
#     if c == 'n':
#         flag = False
# print(polzov)
#
# def san(username, username2):
#     '''Выводит приветствие'''
#     print('Hello ' + username.title() + username2 + ' !')
# san('Сергей', 'Небишь')
#
# def book(name):
#     print('Моя любимая книга это рассказы ' + name)
# book('Чехов')

def make_album(name_art, name_alb, dor='10'):
    a = {'артист': name_art, 'альбом': name_alb, 'дорожек': dor, }
    return a


print(make_album())
