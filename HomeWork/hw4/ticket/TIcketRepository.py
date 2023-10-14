from HomeWork.hw4.ticket.ItciketRepo import IticketRepo
from HomeWork.hw4.ticket.Ticket import Ticket


class Ticketrepository(IticketRepo):

    tickets: list[Ticket]

    def __init__(self):
        self.tickets = []

    def creaty(self, ticket: Ticket):
        self.tickets.append(ticket)

    def read(self, ticket: Ticket):
        if ticket in self.tickets:
            return ticket
        else:
            return

    def delete(self, ticket: Ticket):

        if ticket in self.tickets:
            self.tickets.remove(ticket)
        else:
            return

    def edit(self, ticket: Ticket):
        pass
