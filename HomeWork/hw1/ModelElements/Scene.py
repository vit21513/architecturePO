from HomeWork.hw1.ModelElements import Camera
from HomeWork.hw1.ModelElements.Flash import Flash
from HomeWork.hw1.ModelElements.PoligonalModel import PoligonalModel


class Scene:
    cameras: list[Camera]

    def __init__(self, id: int, models: list[PoligonalModel], flashes: list[Flash], cameras: list[Camera]):
        self.id = id
        if len(models) > 0:
            self.models = models
        else:
            raise Exception('должна быть хоть одна модель')
        self.flashes = flashes
        self.cameras = cameras

    def method1(self, obj: object):
        return obj

    def method2(self, obj: object, obj2: object):
        result = object()
        return result
