"""
Lambdas are one line functions.
They are also known as anonymous functions in some other languages.
You might want to use lambdas when you don’t want to use a function twice in a program.
They are just like normal functions and even behave like them.
"""

# lambda argument: manipulate(argument)

add = lambda x, y: x + y

print(add(3, 5))

# list sorting
a = [(1, 2, 3), (4, 1, 4), (9, 10, 5), (13, -3, 6)]
a.sort(key=lambda x: x[2])  # sorts by 3rd key in tuple
# key= Optional. A function to specify the sorting criteria(s)

'''
# A function that returns the length of the value:
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
'''

print(a)

asd = lambda x: x[2]
print(asd(a))


#Parallel sorting of lists
list1 = [(5, 2, 3), (1, 2, 4), (9, 2, 5), (13, -3, 6)]
list2 = [(5, 2, 3), (4, 1, 4), (9, 10, 5), (13, -3, 6)]

data = zip(list1, list2)
list1, list2 = map(lambda t: list(t), zip(*data))
print(list1)
print(list2)