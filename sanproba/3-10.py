names = ['Света', 'Люба', 'Таня', 'Оля', 'Олеся']
print(names)

print('Представим временно эти имена в алфавитном порядке')
print(sorted(names))
print('Представим временно эти имена в обратном алфавитном порядке')
print(sorted(names, reverse=True))

print('Представим имена в обратном порядке')
# Не работает, если сразу вставлять в print(names.reverse()) Не знаю почему. Выдает Null
names.reverse()
print(names)
print('Вернем имена в исходный порядок')
names.reverse()
print(names)

print('Добавим имя в конец списка')
names.append('Варя')
print(names)
print('Добавим число в конец списка')
names.append(2)
print(names)

print('Удалим число из списка')
del names[-1]
print(names)

print('Удалим элемент списка по известному значению')
names.remove('Варя')
print(names)

print('Вставим новый элемент списка со сдвигом элементов')
names.insert(0, 'Барбара')
print(names)

print('Заменим один элемент списка новым элементом')
names[0] = 'Варвара'
print(names)

print('Узнаем сколько всего элементов в списке')
print('Всего в списке', len(names), 'элементов')

print('Ошибка индекс. при попытке обращения к элементу с отсутствующим индексом - элементов 6, но индекс с 0 до 5')
print(names[6])

