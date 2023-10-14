class BankAcount:
    _card: int
    _balance: float

    def __init__(self, card, balance):
        self._card = card
        self._balance = balance

    def get_card(self):
        return self._card

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        self._balance = balance
