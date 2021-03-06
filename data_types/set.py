"""
Множество в python - "контейнер", содержащий не повторяющиеся элементы в случайном порядке.
С множествами можно выполнять множество операций: находить объединение, пересечение...

len(s) - число элементов в множестве (размер множества).
x in s - принадлежит ли x множеству s.
set.isdisjoint(other) - истина, если set и other не имеют общих элементов.
set == other - все элементы set принадлежат other, все элементы other принадлежат set.
set.issubset(other) или set <= other - все элементы set принадлежат other.
set.issuperset(other) или set >= other - аналогично.
set.union(other, ...) или set | other | ... - объединение нескольких множеств.
set.intersection(other, ...) или set & other & ... - пересечение.
set.difference(other, ...) или set - other - ... - множество из всех элементов set, не принадлежащие ни одному из other.
set.symmetric_difference(other); set ^ other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
set.copy() - копия множества.
И операции, непосредственно изменяющие множество:

set.update(other, ...); set |= other | ... - объединение.
set.intersection_update(other, ...); set &= other & ... - пересечение.
set.difference_update(other, ...); set -= other | ... - вычитание.
set.symmetric_difference_update(other); set ^= other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
set.add(elem) - добавляет элемент в множество.
set.remove(elem) - удаляет элемент из множества. KeyError, если такого элемента не существует.
set.discard(elem) - удаляет элемент, если он находится в множестве.
set.pop() - удаляет первый элемент из множества. Так как множества не упорядочены, нельзя точно сказать, какой элемент будет первым.
set.clear() - очистка множества.
"""

my_set = set('hello')

my_set.add('hi')

print(my_set)  # {'o', 'h', 'l', 'e', 'hi'}

my_set.add('hi')  # already there, wont be added and no exception

words = ['hello', 'daddy', 'hello', 'mum']
words = set(words)
print(words)  # {'hello', 'mum', 'daddy'}
