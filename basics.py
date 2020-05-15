for index in range(0, 3):
    print(index)

for index in range(3):
    print(index)

index = 0
while index < 3:
    index += 1
    print(index)

# functions
from datetime import datetime


def print_time():
    print(datetime.now())


def function_user(func):
    func()


def returner():
    return 1, "2"


def param_default_value(one_param, param_with_default=True):
    print(one_param, param_with_default)


print_time()
function_user(print_time)
first, second = returner()
print(first, second)

param_default_value(1)
# param_default_value() will throw TypeError exception

# named params
param_default_value(param_with_default=False, one_param=second)

param_default_value(param_with_default='not bool', one_param=second)  # will not throw exception BUT THIS IS SHIT

print('------------------ Variables are not mutable -------------------------')


def mutate_var(var):
    var = + var


v = 1
mutate_var(v)

print(v)

print('------------------ Class objects are mutable -------------------------')


class MutatedClass:
    def __init__(self, l, v):
        self.list = l
        self.var = v

    def __repr__(self):
        return '{}, {}'.format(self.list, self.var)


def mutate_class_obj(c: MutatedClass, list, var):
    c.list = list
    c.var = var


obj = MutatedClass([1, 2], "initial")
mutate_class_obj(obj, [2, 3], "mutated")
print(obj)

print('----------------------------------------------------')

# ternary
# Program to demonstrate conditional operator
a, b = 10, 20

# Copy value of a in min if a < b else copy b
min = a if a < b else b

print(min)

for i in 'hello world':
    if i == 'a':
        break
else:
    print('Буквы a в строке нет')
# Буквы a в строке нет
