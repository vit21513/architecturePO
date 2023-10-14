
from HomeWork.hw4.user.User import User
from HomeWork.hw4.user.UserRepository import Userrepository


class Userprovider():

    def __init__(self, base: Userrepository):
        self.base = base

    def get_ticket(self, user: User):
        return self.base.read(user)

    def edit_ticket(self, user: User):
        return self.base.edit(User)

    def delete_ticket(self, user: User):
        return self.base.delete(user)

    def creaty_ticket(self, id, userName, hashPassword, cardNumber):
        self.base.creaty(User(id, userName, hashPassword, cardNumber))
