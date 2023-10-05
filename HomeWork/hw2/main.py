# ДЗ. Добавить новые предметы. Сундуки с новыми предметами.
from random import choice
from HomeWork.hw2.Coins import CoinsGenerator
from HomeWork.hw2.Gems import GemGenerator
from HomeWork.hw2.Gold import GoldGenerator
from HomeWork.hw2.Silver import SilverGenerator


if __name__ == "__main__":
    lst = [GoldGenerator(), GemGenerator(), SilverGenerator(), CoinsGenerator()]
    for i in range(20):
        choice(lst).open_reward()
