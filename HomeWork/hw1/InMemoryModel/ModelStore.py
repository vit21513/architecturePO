import zope

from HomeWork.hw1.InMemoryModel import ImodelChanger
from HomeWork.hw1.InMemoryModel.IModelChangedObserver import IModelChangedObserver
from HomeWork.hw1.ModelElements.Camera import Camera
from HomeWork.hw1.ModelElements.Flash import Flash
from HomeWork.hw1.ModelElements.PoligonalModel import PoligonalModel
from HomeWork.hw1.ModelElements.Scene import Scene


class ModelStore(object):
    zope.interface.implementer(ImodelChanger)
    models: list[PoligonalModel]
    scenes: list[Scene]
    flashes: list[Flash]
    cameras: list[Camera]
    _changedObserver : list[IModelChangedObserver]

    def __init__(self, changedObserver: list[IModelChangedObserver]):
        self._changedObserver = changedObserver
        self.models= PoligonalModel()
        self.scenes =Scene()
        self.flashes =Flash()
        self.cameras =Camera()
        self._changedObserver = list[IModelChangedObserver]

    def getScena(self, num: int) -> Scene:
        result = Scene.method1(num)
        return result

    def notifyChange(self, obj: ImodelChanger):
        pass

    def applyUpdateMode(self):
        pass
