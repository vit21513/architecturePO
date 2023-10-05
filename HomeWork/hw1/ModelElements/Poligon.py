from HomeWork.hw1.ModelElements.Point3D import Point3D


class Poligon:
    points: list[Point3D]

    def __init__(self, points: list[Point3D]):
        self.points = points
