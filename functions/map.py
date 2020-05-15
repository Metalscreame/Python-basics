# map(function_to_apply, list_of_inputs)

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, items))
print(squared)

"""
same as
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)

"""
