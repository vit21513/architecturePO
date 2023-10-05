from HomeWork.hw1.ModelElements.Point3D import Point3D
from HomeWork.hw1.ModelElements.Poligon import Poligon
from HomeWork.hw1.ModelElements.Texture import Texture


class PoligonalModel:

    poligons: list[Poligon]
    textures: list[Texture]

    def __init__(self,textures: list[Texture]):
        self.textures = textures
        PoligonalModel.poligons.append(Poligon(Point3D()))



