def string_returner(name: str) -> str:
    return name


print(string_returner("it's string"))
print(string_returner(1))
print('----------------------------------------------------')


def mutate_data(d):
    for i in range(len(d)):
        d[i] = d[i] * d[i]
    print("d is mutaded")


data = [1, 2, 3]  # lists are mutable

mutate_data(data)
print(data)

data = ("Jeff", "Bill", "Steve", "Mohan")  #
try:
    mutate_data(data)
except TypeError:
    print("Typles are imutable")

print('----------------------------------------------------')


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        def more_local():
            nonlocal spam  # changes in the local scope this var
            spam = "nonlocal spam"

        more_local()

    def do_global():
        global spam  # changes in the module scope this var
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)
print('----------------------------------------------------')
