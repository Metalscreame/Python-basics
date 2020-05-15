class DecoratorExample:
    """ Example Class """

    def __init__(self):
        """ Example Setup """
        print('Hello, World!')
        self.name = 'Decorator_Example'

    def example_function(self):  # Instance method
        """ This method is an instance method! """
        print('I\'m an instance method!')
        print('My name is ' + self.name)


de = DecoratorExample()
de.example_function()


"""
Static methods are methods that are related to a class in some way, but don’t need to access any class-specific data.
 You don’t have to use self, and you don’t even need to instantiate an instance, you can simply call your method:
"""

class DecoratorExample:
    """ Example Class """

    def __init__(self):
        """ Example Setup """
        print('Hello, World!')

    @staticmethod
    def example_function():
        """ This method is a static method! """
        print('I\'m a static method!')


de = DecoratorExample.example_function()

"""
Class methods are the third and final OOP method type to know. Class methods know about their class. 
They can’t access specific instance data, but they can call other static methods.
"""


class DecoratorExample:
    """ Example Class """

    def __init__(self):
        """ Example Setup """
        print('Hello, World!')

    @classmethod
    def example_function(cls):
        """ This method is a class method! """
        print('I\'m a class method!')
        cls.some_other_function()

    @staticmethod
    def some_other_function():
        print('Hello!')


de = DecoratorExample()
de.example_function()
