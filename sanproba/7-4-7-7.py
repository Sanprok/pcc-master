# pizza = []
# b = ''
# while b != 'quit':
#     b = input('Введите дополнения для пиццы, которые вы хотите получить: ')
#     pizza.append(b)
# print('Вы заказали пиццу со следующими дополнениями: ')
# for i in pizza:
#     if i != 'quit':
#         print(i)

small = 3
bigt = 12
zena1 = 'бесплатно'
zena2 = '10 долларов'
zena3 = '15 долларов'
text = 'Цена билета для вас составляет: '
while True:
    a = input('Введите свой возраст: ')
    if a == 'quit':
        print('Вы закончили программу')
        break
    if int(a) < small:
        print(text + zena1)
    elif int(a) >= small and int(a) < bigt:
        print(text + zena2)
    else:
        print(text + zena3)


small = 3
bigt = 12
zena1 = 'бесплатно'
zena2 = '10 долларов'
zena3 = '15 долларов'
text = 'Цена билета для вас составляет: '
active = False
while active  != False:
    a = input('Введите свой возраст: ')
    if a == 'quit':
        print('Вы закончили программу')
        active == True
    if int(a) < small:
        print(text + zena1)
    elif int(a) >= small and int(a) < bigt:
        print(text + zena2)
    else:
        print(text + zena3)