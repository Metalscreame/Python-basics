import math

# print type of math
print(type(math))
# print type of 1
print(type(1))
# print type of "1"
print(type("1"))
# print type of rk
rk = [1, 2, 3, 4, 5, "radha"]
print(type(rk))
print(type(rk[1]))
print(type(rk[5]))

# 2.dir() :This function return list of methods and attributes associated with that object.
# print methods and attributes of rk
print(dir(rk))
rk = (1, 2, 3, 4, 5)

# print methods and attributes of rk
print(dir(rk))
rk = {1, 2, 3, 4, 5}

print(dir(rk))
print(dir(math))
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']

# 3.str() :This function converts everything into a string .


# 4.id() :This function returns a special id of an object.
import math

a = [1, 2, 3, 4, 5]

# print id of a
print(id(a))
b = (1, 2, 3, 4, 5)

# print id of b
print(id(b))
c = {1, 2, 3, 4, 5}

# print id of c
print(id(c))
print(id(math))

# 139787756828232
# 139787757942656
# 139787757391432
# 139787756815768

"""
Methods for Code Introspection
FUNCTION	DESCRIPTION
help()	It is used it to find what other functions do
hasattr()	Checks if an object has an attribute
getattr()	Returns the contents of an attribute if there are some.
repr()	Return string representation of object
callable()	Checks if an object is a callable object (a function)or not.
issubclass()	Checks if a specific class is a derived class of another class.
isinstance()	Checks if an objects is an instance of a specific class.
sys()	Give access to system specific variables and functions
__doc__	Return some documentation about an object
__name__	Return the name of the object.
"""
