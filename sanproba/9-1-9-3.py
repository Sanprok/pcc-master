# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print(self.restaurant_name + self.cuisine_type)
#
#     def open_restaurant(self):
#         print('ресторан открыт')
#
#
# restaurant = Restaurant('Москва', 'рыбный')
#
#
# print(restaurant.restaurant_name)
# restaurant.describe_restaurant()
#
# restaurant.open_restaurant()
#
# restaurant1 = Restaurant('Киевский', 'мясной')
# restaurant2 = Restaurant('Варшава', 'рисовый')
#
# restaurant1.describe_restaurant()
# restaurant2.open_restaurant()
# print(restaurant1.restaurant_name)
# print(restaurant2.cuisine_type)

class User:
    def __init__(self, first_name, last_name, age, pol):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.pol = pol


    def describe_user(self):
        print('Фамилия: ' + self.first_name + ' Имя: ' + self.last_name + ' Возраст: ' + str(self.age) + ' лет ' +
              ' пол: ' + self.pol)


    def greet_user(self):
        print('Добро пожаловать ' + self.first_name + ' ' + self.last_name + ' к нам на сайт.')

user = User('Небишь', 'Сергей', 22, 'мужской')
user.describe_user()
user.greet_user()





