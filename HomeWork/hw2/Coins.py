from HomeWork.hw2.fabric import IGameItem, ItemFabric


class CoinsReward(IGameItem):
    def open(self):
        print('Coins')


class CoinsGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return CoinsReward()

