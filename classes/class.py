"""
_single_leading_underscore
Таким способом задаются частные переменные, функции, методы и классы в модуле.
Все, что использует такой способ задания имени, будет проигнорировано в from module import *.

__double_leading_underscore
Двойное подчеркивание (__) используется для искажения имен атрибутов в классе. Если мы создадим метод с именем «__method»
 в классе с именем «ClassName», то вызвать этот метод так: «ClassName.__method» — у нас уже не получится.
"""


class A:
    pass


class B:
    pass


a = A()
if type(a) == A:
    print("a has A type")


class Car:
    # создаем атрибуты класса
    car_count = 0

    # создаем методы класса
    def start(self, name: str, make, model):
        print("Двигатель заведен")
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1


c = Car()
c.start("1", 2, 3)

c.start(1, 2, 3)

print("car count from 1st obg: {}".format(c.car_count))

b = Car()
b.start(1, 3, 4)
print("car count from 2nd obg: {}".format(b.car_count))

# no field in class - it works
c.im_not_here = 1

print(c.im_not_here)

try:
    print(c.not_there)
except AttributeError:
    print("cant read not initialized field")
