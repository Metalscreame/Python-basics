class Fib:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        while True:
            yield self.a
            self.a, self.b = self.b, self.a + self.b


f = iter(Fib())
for i in range(3):
    print(next(f))


def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


for char in rev_str("hello"):
    print(char)
