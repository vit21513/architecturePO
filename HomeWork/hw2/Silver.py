from HomeWork.hw2.fabric import IGameItem, ItemFabric


class SilverReward(IGameItem):
    def open(self):
        print('Silver')


class SilverGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return SilverReward()

