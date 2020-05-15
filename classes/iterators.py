class Students:
    def __init__(self, s) -> None:
        self._students = s
        self.index = 0

    # must be ovveridem
    def __iter__(self):
        return self

    # must be ovveridem
    def __next__(self):
        if self.index == len(self._students):
            raise StopIteration
        result = 'Current student is: {}'.format(self._students[self.index])
        self.index = self.index + 1
        return result


list = ["Putin", 'Kim Jin']

students = Students(list)

for each in students:
    print(each)



class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration

s_iter2 = SimpleIterator(5)
for i in s_iter2:
    print(i)