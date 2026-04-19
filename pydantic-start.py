# Original code will provide error one by one in case of second user, which is not a great user experience.
# We should be able to get all the problematic fields in one go.
# Also, the code is less maintainable, when the number of parameters or the number of lines increases.
#
# def create_user(username: str, email: str, age: int) -> dict:
#     if not isinstance(username, str): raise TypeError("Username must be a string")
#     if not isinstance(email, str): raise TypeError("Invalid email format")
#     if not isinstance(age, int): raise TypeError("Age must be an integer")

#     return {
#         "username": username,
#         "email": email,
#         "age": age
#     }

# if __name__ == "__main__":
#     user1 = create_user('rohan', 'rohanexample@example.com', 38)
#     print(user1)

#     user2 = create_user('rohan', None, 'old')
#     print(user2)

# Using Pydantic
from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    age: int


if __name__ == "__main__":
    user1 = User(username="rohan", email="rohanexample@example.com", age=38)
    print(user1.model_dump_json())

    # user2 = User(username="rohan", email=None, age="old")
    # print(user2.model_dump_json())
