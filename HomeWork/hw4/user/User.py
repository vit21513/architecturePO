class User:
    id: int
    userName: str
    hashPassword: int
    cardNumber: int

    def __init__(self, id: int, userName: str, hashPassword, cardNumber):
        self._id = id
        self._userName = userName
        self._hashPassword = hashPassword
        self._cardNumber = cardNumber

    def get_id(self):
        return self._id

    def get_userName(self):
        return self._userName

    def get_hash_passwored(self):
        return self._hashPassword
