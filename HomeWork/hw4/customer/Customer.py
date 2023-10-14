from HomeWork.hw4.cash.CashProvider import CashProvider
from HomeWork.hw4.customer.ICustomer import ICustomer
from HomeWork.hw4.ticket.IticketProvider import IticketProvider
from HomeWork.hw4.ticket.Ticket import Ticket
from HomeWork.hw4.user.User import User
from HomeWork.hw4.user.UserprovIder import Userprovider


class Customer(ICustomer):
    ticketProvider: IticketProvider
    cashProvider: CashProvider
    userProvider: Userprovider
    client: User
    tickets: list[Ticket]

    def __init__(self):
        self.cashProvider = CashProvider()
        self.ticketProvider = IticketProvider()
        self.userProvider = Userprovider()

    def get_tickets(self):
        return self.tickets

    def set_tickets(self, tickets: list[Ticket]):
        self.tickets = tickets

    def getUser(self):
        return self.client

    def setUser(self, client: User):
        self.client = client

    def buy_ticket(self, ticket: Ticket):
        pass
