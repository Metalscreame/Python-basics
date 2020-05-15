"""
Единственное отличие set от frozenset заключается в том, что set - изменяемый тип данных, а frozenset - нет.
Примерно похожая ситуация с списками и кортежами.
"""
a = set('qwerty')
b = frozenset('qwerty')
print(a == b)  # True
