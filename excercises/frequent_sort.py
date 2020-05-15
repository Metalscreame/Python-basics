from timeit import timeit


def frequency_sort(items):
    items_dict = {}

    for each in items:
        try:
            items_dict[each] += 1
        except KeyError:
            items_dict[each] = 1

    items_dict = {key: value for key, value in sorted(items_dict.items(), key=lambda item: item[1], reverse=True)}

    result = []
    for key in items_dict.keys():
        result += items_gen(key, items_dict[key])

    return result


def items_gen(item, count) -> list:
    result = []
    for _ in range(count):
        result.append(item)

    return result


def frequency_sort_v2(items):
    return sorted(items, key=lambda x: (-items.count(x), items.index(x)))


from typing import List, Any, Iterator, Union
from collections import Counter

InputData = List[Any]
OutputData = Union[InputData, Iterator[Any]]


def frequency_sort_v3(items: InputData) -> OutputData:  # the fastest
    c = Counter(items)
    result = sorted(c.elements(), key=lambda k: c[k], reverse=True)
    return result


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 2, 2, 2, 6, 6]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")

items = [4, 6, 2, 2, 2, 6, 4, 4, 4]
for f in [frequency_sort, frequency_sort_v2, frequency_sort_v3]:
    t = timeit(stmt="f(items)", number=100, globals=globals())  # says that call
    print(f"{f.__name__} took: {t:.6f}")
