# Модуль collections - предоставляет специализированные типы данных, на основе словарей, кортежей, множеств, списков.

# https://pythonworld.ru/moduli/modul-collections.html
import collections
c = collections.Counter()

for word in ['spam', 'egg', 'spam', 'counter', 'counter', 'counter']:
    c[word] += 1

print(c)

c = collections.Counter(a=4, b=2, c=0, d=-2)
print(c.items())
print(list(c.elements()))


"""
DEQUE

collections.deque(iterable, [maxlen]) - создаёт очередь из итерируемого объекта с максимальной длиной maxlen. 
Очереди очень похожи на списки, за исключением того, что добавлять и удалять элементы можно либо справа, либо слева.
Методы, определённые в deque:

append(x) - добавляет x в конец.
appendleft(x) - добавляет x в начало.
clear() - очищает очередь.
count(x) - количество элементов, равных x.
extend(iterable) - добавляет в конец все элементы iterable.
extendleft(iterable) - добавляет в начало все элементы iterable (начиная с последнего элемента iterable).
pop() - удаляет и возвращает последний элемент очереди.
popleft() - удаляет и возвращает первый элемент очереди.
remove(value) - удаляет первое вхождение value.
reverse() - разворачивает очередь.
rotate(n) - последовательно переносит n элементов из начала в конец (если n отрицательно, то с конца в начало).
"""