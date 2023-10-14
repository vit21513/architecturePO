from HomeWork.hw4.user.User import User
from HomeWork.hw4.user.usertRepo import UserRepo


class Userrepository(UserRepo):

    users: list[User]

    def __init__(self):
        self.users = []

    def creaty(self, user: User):
        self.users.append(user)

    def read(self, user: User):
        if user in self.users:
            return user
        else:
            return

    def delete(self, user: User):

        if user in self.users:
            self.users.remove(user)
        else:
            return

    def edit(self, user: User):
        pass
