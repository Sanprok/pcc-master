# names = ['san', 'admin', 'stern', 'plant']
# if names:
#     for name in names:
#         if name == 'admin':
#             print("Приветствую тебя великий " + name)
#         else:
#             print('Приветствую тебя пользователь ' + name)
# else:
#     print('Список пользователей пуст')


# Не знаю как сверять элементы, если в первом списки разные написания слова, как их преобразовать к нижнему регистру
# для сравн., придумал перебрать все элем., привести их к нижнему рег. и сохр. в новом списке, который уже и сравнивать
sowpaden = []

current_users = ['san', 'admin', 'stern', 'pLant', 'Klava']
new_current_users = []
for i in current_users:
    new_current_users.append(i.lower())
new_users = ['san', 'Admin', 'plant', 'aaaaa', 'KLAVA']
for new_user in new_users:
    if new_user.lower() in new_current_users:
        sowpaden.append(new_user)
        print('имя пользователя - ' + new_user + ' уже зарегистрировано' + '\nВыберете новое имя')
    else:
        print('Имя ' + new_user + ' доступно')

print('Эти именя совпадают ', sowpaden)

ddd = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in ddd:
    if i == 1:
        print(str(i) + 'st')
    elif i == 2:
        print(str(i) + 'nd')
    elif i == 3:
        print(str(i) + 'rd')
    else:
        print(str(i) + 'th')








