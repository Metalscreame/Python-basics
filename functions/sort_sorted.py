# sorted - returns sorted list
# sort - sorts given data

# sort - works only for lists, when sorted works for all iterable
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

    def weighted_grade(self):
        return 'CBA'.index(self.grade) / self.age


student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
sorted(student_objects, key=lambda student: student.age)  # сортируем по возрасту
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

from operator import itemgetter, attrgetter, methodcaller

student_tuples = (('dave', 'B', 22), ('jane', 'B', 12), ('john', 'A', 15))
sorted(student_tuples, key=itemgetter(2))
print(student_tuples)
# (('dave', 'B', 22), ('jane', 'B', 12), ('john', 'A', 15))

vowels = ['e', 'a', 'u', 'o', 'i']
for v in sorted(vowels):
    print(v)