# homo = {
#     'name': 'San',
#     'first_name':  'Neb',
#     'age': '42',
#     'city': 'Kirow',
# }
# print('Его зовут ' + homo['name'] + ' ' + homo['first_name'] + ', ему ' + homo['age'] + ' года, живет в городе ' +
#       homo['city'] + '.')

# frend = {}
# stop = 0
# while stop != 3:
#     aa = input('Введи свое имя')
#     bb = input(aa + ', введи свое любимое число')
#     frend [aa] = bb
#     stop += 1
#
# print(frend)
# dd = input('Введи имя человека, чтобы узнать его любимое число')
# print('Возраст ' + dd + ' ' + frend[dd] + ' лет')

# golosov = {
#     'san': 'ruby',
#     'pit': 'java',
#     'lans': 'python',
# }
# nogolos = ['san', 'pit', 'ROK', 'Sandra']
#
# # Перебир. имена в списке nogolos, если такое имя есть в ключах словаря, то сообщ. об этом, если нет, то предл. ввести
# for ii in nogolos:
#     if ii in golosov.keys():
#         print(ii + " уже принимал участие в голосовании")
#     else:
#         print(ii + ' выберите любимый язык программирования')
#         bb = input()
#         golosov[ii] = bb
# print(golosov)


# golosov = {
#     'san': ['ruby', 'c', ],
#     'pit': ['java', 'c', ],
#     'lans': ['python', 'c', ],
# }
# nogolos = ['san', 'pit', 'ROK', 'Sandra']
#
# # Перебир. имена в списке nogolos, если такое имя есть в ключах словаря, то сообщ. об этом, если нет, то предл. ввести
# for ii in nogolos:
#     if ii in golosov.keys():
#         print(ii + " уже принимал участие в голосовании")
#     else:
#         print(ii + ' выберите любимый язык программирования')
#         bb = input()
#         a = []
#         a.append(bb)
#         golosov[ii] = a
# print(golosov)
# print('Введите свое имя')
# cc = input()
# for i in golosov:
#     if i == cc:
#         print(i + ' выши любимые языки ')
#         for ccc, bbb in golosov.items():
#             if ccc == cc:
#                 print(bbb)




golosov = {
    'san': ['ruby', 'c', ],
    'pit': ['java', 'c', ],
    'lans': ['python', 'c', ],
}
nogolos = ['san', 'pit', 'ROK', 'Sandra']

# Перебир. имена в списке nogolos, если такое имя есть в ключах словаря, то сообщ. об этом, если нет, то предл. ввести
for ii in nogolos:
    if ii in golosov.keys():
        print(ii + " уже принимал участие в голосовании")
    else:
        print(ii + ' выберите любимый язык программирования')
        bb = input()
        a = []
        a.append(bb)
        golosov[ii] = a
print(golosov)
print('Введите свое имя')
ddd = input()
for ccc, bbb in golosov.items():
    if ccc == ddd:
        if len(bbb) > 1:
            print(ccc + ' ваши любимые языки ')
        else:
            print(ccc + ' ваш единственный язык это ')
        print(bbb)




