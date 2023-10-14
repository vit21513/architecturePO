from HomeWork.hw4.bank.BankAccount import BankAcount
from HomeWork.hw4.cash.icashrepo import icashrepo


class CashRepository(icashrepo):
    clients = [BankAcount]

    def __init__(self):
        self.clients = []
        self.clients.append(BankAcount())

    def get_CashRepository(self):
        return CashRepository()

    def transaction(self,payment:int):
        pass