"""
Comprehensions are a feature of Python which I would really miss if I ever have to leave it.
Comprehensions are constructs that allow sequences to be built from other sequences.
Several types of comprehensions are supported in both Python 2 and Python 3:

list comprehensions
dictionary comprehensions
set comprehensions
generator comprehensions

We will discuss them one by one. Once you get the hang of using list comprehensions then you can use any of them easily.
"""

# variable = [out_exp for out_exp in input_list if out_exp == 2]

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

squared = []
for x in range(10):
    squared.append(x ** 2)

# the same as
squared = [x ** 2 for x in range(10)]


def expressions(i):
    return i


new_list = []
old_list = [1, 2]
for i in old_list:
    if filter(i):
        new_list.append(expressions(i))

# same as
new_list = [expressions(i) for i in old_list if filter(i)]

"""
>>> squares = [i * i for i in range(10)]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
"""


"""
filter without filter
>>> sentence = 'the rocket came back from mars'
>>> vowels = [i for i in sentence if i in 'aeiou']
>>> vowels

['e', 'o', 'e', 'a', 'e', 'a', 'o', 'a']
"""


"""
new_list = [expression (if conditional) for member in iterable]
С помощью этого шаблона вы можете использовать условную логику для выбора из нескольких возможных вариантов вывода.
Например, если у вас есть список цен, вы можете заменить отрицательные цены на 0 и оставить положительные значения без изменений:

>>> original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
>>> prices = [i if i > 0 else 0 for i in original_prices]
>>> prices
[1.25, 0, 10.22, 3.78, 0, 1.16]
"""