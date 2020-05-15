class Abstracter:
    def __init__(self):
        pass

    def some_method(self):
        pass


class Implementator(Abstracter):
    def __init__(self, val):
        self.val = val

    def some_method(self):
        print("lel")
