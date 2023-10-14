from abc import ABC,abstractmethod


class icashrepo(ABC):

    @abstractmethod
    def transaction(self, num: int):
        pass