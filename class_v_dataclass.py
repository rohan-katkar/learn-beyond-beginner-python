from dataclasses import dataclass

@dataclass
class MyDClass:
    name: str
    roll: int

class MyNClass:
    name: str
    roll: int

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def __repr__(self):
        return f"MyNClass[name = {self.name}, roll = {self.roll}]"

if __name__ == "__main__":
    dclass = MyDClass("rohan", 10)
    print(dclass)

    nclass = MyNClass("rohan", 10)
    print(nclass)