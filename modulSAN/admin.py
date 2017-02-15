class User:
    def __init__(self, first_name, last_name, age, pol, login_attempts=0, number_served=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.pol = pol
        self.number_served = number_served
        self.login_attempts = login_attempts

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print('Фамилия: ' + self.first_name + ' Имя: ' + self.last_name + ' Возраст: ' + str(self.age) + ' лет ' +
              ' пол: ' + self.pol)

    def greet_user(self):
        print('Добро пожаловать ' + self.first_name + ' ' + self.last_name + ' к нам на сайт.')

    def set_number_served(self):
        a = int(input('Введите пробег: '))
        if a >= self.number_served:
            print('Мы учли ваш пробег')
            self.number_served = a
        else:
            print('Вы пытаетесь скрутить пробег')

    def increment_number_served(self):
        self.number_served += 100


class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges


class Admin(User):
    def __init__(self, first_name, last_name, age, pol, login_attempts=0, number_served=0):
        super().__init__(first_name, last_name, age, pol, login_attempts=0, number_served=0)
        self.privileges = Privileges([])