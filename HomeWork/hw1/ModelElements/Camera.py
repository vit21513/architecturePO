from HomeWork.hw1.ModelElements.Angle3D import Angle3D
from HomeWork.hw1.ModelElements.Point3D import Point3D


class Camera:
    location: Point3D
    angle: Angle3D

    def rotate(self, obj: Angle3D):
        pass

    def move(self, obj: Point3D):
        pass
