import datetime


class Ticket:
    id: int
    price: float
    place: int
    data: datetime.datetime
    is_valid: bool

    def __init__(self, id: int, price: float, place: int, data: datetime.datetime, is_valid: bool):
        self._id = id
        self._price = price
        self._place = place  # место билета
        self._data = data
        self._is_valid = is_valid  # true свободное место false - занято

    def get_id(self):
        return self._id

    def set_id(self, num: int):
        self._id = num

    def get_price(self):
        return self._price

    def set_price(self, new_price: int):
        self._price = new_price

    def get_place(self):
        return self._place

    def set_place(self, new_place: int):
        self._place = new_place

    def get_data(self):
        return self._data

    def set_date(self, data):
        self._data = data

    def set_valid(self, is_valid):
        self._is_valid = is_valid

    def get_valid(self):
        return self._is_valid

    def __str__(self):
        return f'билет id {self._id} price {self._price} data {self._data}  статус {self._is_valid} '
