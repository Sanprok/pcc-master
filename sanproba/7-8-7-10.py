# sandwich_orders = [
#     'sarm', 'parm', 'darm', 'prot', 'pastrami', 'pastrami', 'pastrami',
# ]
# finished_sandwiches = []
# print('Pastrami уже закончились')
# while 'pastrami' in sandwich_orders:
#     # Удаление значения из списка по его значению, а не по индексу
#     sandwich_orders.remove('pastrami')
# while sandwich_orders:
#     a = sandwich_orders.pop()
#     finished_sandwiches.append(a)
#     print('Я предлагаю сендвич под названием: ' + a)
# b = len(finished_sandwiches)
# print('Я дал вам ' + str(b) + ' сендвичи')
# for i in finished_sandwiches:
#     print(i)

polzow = [
    'san', 'piter', 'serg', 'vovan',
]
lov_gor = {}
for i in polzow:
    a = input(i + ', где бы выхотели провести отпуск? Введите название города: ')
    lov_gor[i] = a
print('Результаты голосования следующие: ')
for bb, cc in lov_gor.items():
    print(bb + ' хотел бы отдохнуть в городе ' + cc)

