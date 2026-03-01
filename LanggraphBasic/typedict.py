####typ hints---.typed hints

from typing import TypedDict
from typing import Union
from typing import Any
from typing import Optional


class Movie(TypedDict):
    name: str
    year: int


movie = Movie(name="advengers Endgame", year=2019)
print(movie)


###---- Union -----
## x can be either int or float
def Square(x: Union[int, float]) -> float:
    return x * x


print(Square(5.5))

###---- Optional -----


def nice_message(name: Optional[str]) -> None:
    if name is None:
        print("Hey random person !")
    else:
        print(f"Hi there, {name}")
