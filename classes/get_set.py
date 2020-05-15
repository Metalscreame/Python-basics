class Obj:
    """property demo"""

    def __init__(self, attr):
        self._attribute = attr

    @property
    def attribute(self):  # implements the get - this name is *the* name
        return self._attribute

    @attribute.setter
    def attribute(self, value):  # name must be the same
        self._attribute = value

    @attribute.deleter
    def attribute(self):  # again, name must be the same
        del self._attribute


obj = Obj(1)
obj.attribute = 2
the_value = obj.attribute
del obj.attribute

# НО это не питоник вэй