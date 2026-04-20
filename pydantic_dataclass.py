"""
Pydantic provides dataclass same as original builtin dataclass. Some of the functionalities are similar.
You have to call dataclass from pydantic module.
__init__ is already created as a part of pydantic module, so there is no need to add.
Similar to builtin dataclass, it provides same methods as attributes.
"""

from pydantic.dataclasses import dataclass


@dataclass
class PydDataclass:
    name: str

    def __repr__(self):
        return f"The name is {self.name}"


if __name__ == "__main__":
    try:
        myname = PydDataclass("rohan")
        print(myname)
    except Exception as e:
        print(e)
