from dataclasses import dataclass


# adding __init__ and __repr__
@dataclass
class Number:
    val: int
    count: int = 0  # default value


# same as above
class NumberTwo:
    def __init__(self, val):
        super().__init__()
        self.val = val

    def __repr__(self) -> str:
        return super().__repr__()


n = Number(val=1, count=2)

print(n.val)
print(n)

n = NumberTwo(1)

print(n.val)
print(n)
