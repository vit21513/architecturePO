# isp

from math import pi

from HomeWork.hw3.isp.Shape import Shape


class Circle(Shape):

    def __init__(self, radius: int | float):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


if __name__ == "__main__":
    one = Circle(5)
    print(one.area())
