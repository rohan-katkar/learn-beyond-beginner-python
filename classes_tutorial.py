from dataclasses import dataclass

class MyClass:
    def __init__(self):
        pass

    def __my_private_method(self):
        print("This is a private method")

    def my_class_method(self):
        print(self)
        # print(__name__)
        print("This is a class method.")
        # self.__my_private_method()        

    @staticmethod
    def my_static_method():
        print("This is a static method")

if __name__ == "__main__":
    myclass1 = MyClass()
    myclass1.my_class_method()