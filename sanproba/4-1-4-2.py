pizzas = ['super', 'alg', 'mart']
lov = 'Я люблю пиццу '
for pizza in pizzas:
    print(lov + pizza.title())
print('А еще больше я люблю пельмени')
frend_pizzas = pizzas[:]
frend_pizzas.append('RRRR')
pizzas.append('AAAA')
print(frend_pizzas)
print(pizzas)
pp= 'Мой список любимых пицц: '
print(pp)
[print(i.title()) for i in pizzas]




mleks = ['собака', 'кошка', 'шиншилла']
for mlek in mleks:
    print('У меня есть', mlek)
print('Это все мои любимые домашние животные')


