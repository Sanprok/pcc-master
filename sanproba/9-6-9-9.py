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
# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuicine_type):
#         super().__init__(restaurant_name, cuicine_type)
#         self.flavors = []
#
#
#     def printFlavors(self):
#         for i in self.flavors:
#             print(i)
#         print(list(self.flavors))
#
#
# iceCream = IceCreamStand('Московский', 'мясной')
# b = ['san', 'adf', 'adf']
# iceCream.flavors = b
# iceCream.printFlavors()



# class User:
#     def __init__(self, first_name, last_name, age, pol, login_attempts=0, number_served=0):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.pol = pol
#         self.number_served = number_served
#         self.login_attempts = login_attempts
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print('Фамилия: ' + self.first_name + ' Имя: ' + self.last_name + ' Возраст: ' + str(self.age) + ' лет ' +
#               ' пол: ' + self.pol)
#
#     def greet_user(self):
#         print('Добро пожаловать ' + self.first_name + ' ' + self.last_name + ' к нам на сайт.')
#
#     def set_number_served(self):
#         a = int(input('Введите пробег: '))
#         if a >= self.number_served:
#             print('Мы учли ваш пробег')
#             self.number_served = a
#         else:
#             print('Вы пытаетесь скрутить пробег')
#
#     def increment_number_served(self):
#         self.number_served += 100
#
#
# class Privileges():
#     def __init__(self, privileges):
#         self.privileges = privileges
#
#
# class Admin(User):
#     def __init__(self, first_name, last_name, age, pol, login_attempts=0, number_served=0):
#         super().__init__(first_name, last_name, age, pol, login_attempts=0, number_served=0)
#         self.privileges = Privileges([])
#
#
# admin = Admin('Небишь', 'Сергей', 22, 'мужской', )
# admin.privileges.privileges = ['разрешено добавлять сообщения', 'разрешено удалять пользователей',
#                                'разрешено банить пользователей']
# print(admin.privileges.privileges)


"""A set of classes that can be used to represent electric cars."""


class Car():
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=60):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size !=85:
            self.battery_size = 85




class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

electricCar = ElectricCar('заз', 'шанс', '2000')
electricCar.battery.describe_battery()
electricCar.battery.get_range()
electricCar.battery.upgrade_battery()
electricCar.battery.get_range()
