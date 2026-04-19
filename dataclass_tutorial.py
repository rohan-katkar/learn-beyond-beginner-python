from dataclasses import dataclass, field

@dataclass
class MyDataClass:
    """Class for testing dataclass"""
    name: str
    unit_price: float
    quantity_on_hand: int = 0
    sizes: list[str] = field(default_factory=list)

    # Init, Represent, Equals and other magic/double-underscore methods are automatically created

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

@dataclass
class Square(Rectangle):
    side: float

    def __post_init__(self):        # dataclass does not call and non-dataclass init method, hence explicit
        super().__init__(self.side, self.side)


if __name__ == "__main__":
    dataclass1 = MyDataClass('rohan', 100.00, 50)
    print(dataclass1.total_cost())
    print(dataclass1.sizes)