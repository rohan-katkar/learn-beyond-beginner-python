"""
Field inside Annotated class will allow us to set a specific range, or provide strict checking of the input.
"""

from typing import Annotated

from pydantic import BaseModel, Field


class Model(BaseModel):
    roll_num: Annotated[int, Field(ge=0, le=100)]


if __name__ == "__main__":
    try:
        model = Model(roll_num=10)
        print(model)
    except Exception as e:
        print(e)
