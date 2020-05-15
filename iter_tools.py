import itertools
import time

from usefull_functions import current_milli_time, elapse_time

data = [5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2,
        6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4,
        5, 9, 1, 5, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 1, 5, 2,
        6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 1,
        5, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9,
        1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2,
        6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4,
        5, 9, 1, 5, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 1, 5, 2,
        6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 1,
        5, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9,
        1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2,
        6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4,
        5, 9, 1, 5, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 1, 5, 2,
        6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 1,
        5, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9,
        1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2,
        6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4,
        5, 9, 1, 5, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 1, 5, 2,
        6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 1,
        5, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9,
        1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2,
        6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4,
        5, 9, 1, 5, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 1, 5, 2,
        6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 1,
        5, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9,
        1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2,
        6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4, 5, 9, 1, 5, 2, 6, 4,
        5, 9, 1, 5, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 1, 5, 2,
        6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 1,
        5, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 15, 2, 6, 4, 5, 9, 1]

start_time = time.time()

sum = 0
for i in range(len(data)):
    sum += data[i]
    print(sum)

t = elapse_time(start_time)
print("Without itertools took {}".format(current_milli_time(t)))

start_time = time.time()

result = itertools.accumulate(data)

for each in result:
    print(each)

t = elapse_time(start_time)
print("With itertools took {}".format(current_milli_time(t)))

# iteramte over merged iterables
list_one = ["1"]
list_two = ["2"]
list_three = ["3"]
for item in itertools.chain(list_one, list_two, list_three):
    print(item)
