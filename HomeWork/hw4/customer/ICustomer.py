from abc import ABC, abstractmethod

from HomeWork.hw4.ticket.Ticket import Ticket
from HomeWork.hw4.user.User import User


class ICustomer(ABC):

    @abstractmethod
    def get_tickets(self):
        pass

    @abstractmethod
    def getUser(self):
        pass

    @abstractmethod
    def setUser(self, client: User):
        pass

    @abstractmethod
    def buy_ticket(self, ticket: Ticket):
        pass
