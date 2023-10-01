import zope

from HomeWork.hw1.InMemoryModel import ImodelChanger
from HomeWork.hw1.InMemoryModel.IModelChangedObserver import IModelChangedObserver
from HomeWork.hw1.ModelElements.Camera import Camera
from HomeWork.hw1.ModelElements.Flash import Flash
from HomeWork.hw1.ModelElements.PoligonalModel import PoligonalModel
from HomeWork.hw1.ModelElements.Scene import Scene


class ModelSrore:
    zope.interface.implements(IModelChangedObserver, ImodelChanger)
    models = list[PoligonalModel]
    scenes = list[Scene]
    flashes = list[Flash]
    cameras = list[Camera]


    def getScena(self, num: int) -> Scene:
        result = Scene.method1(num)
        return result

    def notifyChange(self, obj: ImodelChanger):
        pass

    def applyUpdateMode(self):
        pass
