from HomeWork.hw4.carier.Carirerrepository import Carrierrepository
from HomeWork.hw4.cash.CashRepository import CashRepository


class CashProvider:
    cardNumber: int
    cashRepository: CashRepository
    carrierRepository: Carrierrepository

    def __init__(self):
        self.carrierRepository = Carrierrepository.get_Carrierrepository()
        self.cashRepository = CashRepository.get_CashRepository()

    def buy_ticket(self):
        pass
