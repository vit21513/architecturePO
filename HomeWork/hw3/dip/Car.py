from HomeWork.hw3.dip.Diesel import Diesel
from HomeWork.hw3.dip.Engine import Engine
from HomeWork.hw3.dip.Petrol import Petrol


class Car(Engine):

    def __init__(self, engine: Diesel | Petrol):
        self.engine = engine

    def start_engine(self):
        self.engine.start_engine()


if __name__ == "__main__":
    petrol_engine = Petrol()
    diesel_engine = Diesel()
    car1 = Car(petrol_engine)
    car2 = Car(diesel_engine)
    car1.start_engine()
    car2.start_engine()
