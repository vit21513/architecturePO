from abc import ABC, abstractmethod


class Engine(ABC):

    @abstractmethod
    def start_engine(self):
        pass
