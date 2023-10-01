from HomeWork.hw1.ModelElements.Angle3D import Angle3D
from HomeWork.hw1.ModelElements.Color import Color
from HomeWork.hw1.ModelElements.Poligon import Point3D


class Flash:
    location: Point3D
    angle: Angle3D
    color: Color
    power: float

    def rotate(self, obj: Angle3D):
        pass

    def move(self, obj: Point3D):
        pass
