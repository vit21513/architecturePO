class Carrier:
    _id: int
    _cardnumber: int

    def __init__(self, id, cardNumber):
        self._id = id
        self._cardnumber = cardNumber

    def get_id(self):
        return self._id

    def get_cardnumber(self):
        return self._cardnumber
