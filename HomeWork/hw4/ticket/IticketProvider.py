from datetime import datetime
from HomeWork.hw4.ticket.TIcketRepository import Ticketrepository
from HomeWork.hw4.ticket.Ticket import Ticket


class IticketProvider:



    def __init__(self, base:Ticketrepository):
        self.base = base

    def get_ticket(self, ticket:Ticket):
        return self.base.read(ticket)

    def edit_ticket(self, ticket: Ticket):
        return self.base.edit(ticket)

    def delete_ticket(self, ticket):
        return self.base.delete(ticket)

    def creaty_ticket(self, id: int, price: float, place: int, data: datetime, is_valid: bool):
        self.base.creaty(Ticket(id, price, place, data, is_valid))
