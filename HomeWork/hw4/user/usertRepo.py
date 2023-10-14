from abc import ABC,abstractmethod

from HomeWork.hw4.user.User import User


class UserRepo(ABC):

    @abstractmethod
    def creaty(self, num:int):
        pass

    @abstractmethod
    def read(self,user:User):
        pass

    @abstractmethod
    def delete(self,user:User):
        pass

    @abstractmethod
    def edit(self, user:User):
        pass
