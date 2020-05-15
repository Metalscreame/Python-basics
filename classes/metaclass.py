class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)

        # lets change name of attrs
        atrs = {}

        for name, value in attrs.items():
            if name.startswith("__"):
                atrs[name] = value
            else:
                atrs[name.upper()] = value

        return type(class_name, bases, atrs)


class Dog(metaclass=Meta):
    will_be_capitalized_by_meta = True

    def __init__(self, x, y):
        self.not_be_capitalized_by_meta = x
        self.y = y

    def some_func(self):
        print("func")


# type(name, bases, attrs)


d = Dog(x=5, y=8)

# d will have all attrs capitalized because of meta class creation
print(d.SOME_FUNC)
print(d.WILL_BE_CAPITALIZED_BY_META)
