#  the list is a collection of items of different data types. It is an ordered sequence of items
list = [3, 2, 5, "3", True]

print(list)
list = [3, 2, 5]
list.sort()
list.append(4)
list.insert(0, 50)
print(list)

list1 = list
list2 = list
list1.extend(list2)
print(list1)

print("Number of occurences of number {} in list1 is {}".format(3, list1.count(3)))

del list  # deletes list

# Tuple is a collection of items of any Python data type, same as the list type.
# Unlike the list, tuple is immutable.
typles = ("Jeff", "Bill", "Steve", "Mohan")

# A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.
dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "object": {
        "list": [1, 2, 3],
    }
}
print(dict)
print(dict["brand"])
print(dict["object"]["list"])

for key in dict:
    print('{}:{}'.format(key, dict[key]))
# same as
for key, value in dict.items():
    print('{}:{}'.format(key, value))

from array import array
#used only for digits
numbers = array('d')  # digit
numbers.append(1)
numbers.append(2)
print(numbers.__len__())
