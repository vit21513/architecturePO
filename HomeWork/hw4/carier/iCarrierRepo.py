from abc import ABC, abstractmethod


class ICarrierRepo(ABC):

    @abstractmethod
    def read(self,num:int):
        pass


