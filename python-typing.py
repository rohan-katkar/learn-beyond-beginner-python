"""Python typing module performs annotations only. It does not enforce the types provided.
It will also allows your IDE to perform syntax highlighting and intellisense to provide proper methods.
It will also allow static type checking with tools like mypy.
Remember, python works on 'explicit rather than implicit' philosophy.
Hence, it is generally good practice to show that certain types are optional.

Optional: Install mypy for static type checking on command line. Syntax: mypy <file-name>"""

x: int = 1          # int here is a hint

def sum_numbers(x: int, y: int, z: int) -> int:         # -> will allow us to hint the type of return value
    return x + y + z

# Before python 3.8, this gave issue.
y: list[list[int]] = [[1, 2, 4], [4, 5, 6]]
# print(y)

# Before python 3.8, this gave issue.
z: dict[str, str] = {"a": "b"}
# print(z)

# Custom type creation
from typing import List
Vector = List[float]
Vectors = List[Vector]

def foo(v: Vectors) -> Vector:
    pass

foo([[1, 2, 4], [4, 5, 6]])

# Optional types - means that the value can be either True, False or None
# Originally
def foo0(order: bool | None):
    pass

# With Optional
from typing import Optional
def foo1(order : Optional[bool]):
    pass

foo1()

# Sequence - Any list, tuple, set that can be accessed
from typing import Sequence
def foo2(seq: Sequence[str]):
    pass

foo2(("1", "2", "3"))
foo2(["1", "2", "3"])

# Callable - if you want to call a function as argument to parameter
from typing import Callable
def foo3(func: Callable[[int], int]):       # needs parameters in [] and return type as separate
    pass

def foo4() -> Callable[[int], int]:         # nested function, return the same
    def add(x: int, y: int):
        return x + y
    
    return add


# Generics - learn more in future
from typing import TypeVar
T = TypeVar('T')

def get_item(lst: List[T], index: int) -> T:
    return lst[index]