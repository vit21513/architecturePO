from HomeWork.hw3.isp.Shape import Shape
from HomeWork.hw3.isp.Shape3D import Shape3D


class Cube(Shape, Shape3D):

    def __init__(self, edge: int | float):
        self.edge = edge

    def area(self):
        return 6 * self.edge ** 2

    def volume(self):
        return self.edge ** 3


if __name__ == "__main__":
    one = Cube(5)
    print(one.area())
    print(one.volume())
