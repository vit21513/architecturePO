from HomeWork.hw4.carier.Carrier import Carrier
from HomeWork.hw4.carier.iCarrierRepo import ICarrierRepo


class Carrierrepository(ICarrierRepo):

    carrrier = list[Carrier]

    def __init__(self):
        self.carrrier = []

    def get_Carrierrepository(self):
        return self.carrrier

    def read(self, id: int):
        for obj in self.carrrier:
            if obj.get_id() == id:
                return obj
        return Exception("not found carrier")

