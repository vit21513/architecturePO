from abc import ABC,abstractmethod

from HomeWork.hw4.ticket.Ticket import Ticket


class IticketRepo(ABC):

    @abstractmethod
    def creaty(self, odj:Ticket):
        pass

    @abstractmethod
    def read(self,ticket:Ticket):
        pass

    @abstractmethod
    def delete(self,ticket:Ticket):
        pass

    @abstractmethod
    def edit(self, ticket:Ticket):
        pass
