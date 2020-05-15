# В Pyhon функция zip позволяет пройтись одновременно по нескольким итерируемым объектам (спискам и др.):

a = [10, 20, 30, 40]
b = ['a', 'b', 'c', 'd', 'e']

for i, j in zip(a, b):
    print(i, j)  # (10, a)

zip_obj = zip(a, b)

list_zip = list(zip_obj)  # list of tuples
print(list_zip)
