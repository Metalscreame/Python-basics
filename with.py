from contextlib import contextmanager


@contextmanager
def opened(filename, mode="r"):
    f = open(filename, mode)
    try:
        # this is step 0,
        yield f # file is yielded in the with statement
    finally:
        print("2 closing file")
        f.close()


# with will open a file, yeild data, and then close it
with opened("date.py") as file:
    for line in file:
        print(line.rstrip())
    print("1 finishing with statement")

print("3 finished program")

