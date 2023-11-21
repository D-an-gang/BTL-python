import datetime
import random


class Merchandise:
    id: int
    name: str
    price: float
    import_price: float  # giá nhập
    quantity: int
    mfg: datetime.date  # ngày sản xuất
    exp: datetime.date  # hạn sử dụng

    def __init__(self):
        pass
        # Getter methods

    def __init__(self, name: str, price: float, import_price: float, quantity: int, mfg: datetime.date,
                 exp: datetime.date):
        self.id = random.randint(0, 9999)
        self.name = name
        self.price = price
        self.import_price = import_price
        self.quantity = quantity
        self.mfg = mfg
        self.exp = exp

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_import_price(self):
        return self.import_price

    def get_quantity(self):
        return self.quantity

    def get_mfg(self):
        return self.mfg

    def get_exp(self):
        return self.exp

    # Setter methods
    def set_id(self, new_id):
        self.id = new_id

    def set_name(self, new_name):
        self.name = new_name

    def set_price(self, new_price):
        self.price = new_price

    def set_import_price(self, new_import_price):
        self.import_price = new_import_price

    def set_quantity(self, new_quantity):
        self.quantity = new_quantity

    def set_mfg(self, new_mfg):
        self.mfg = new_mfg

    def set_exp(self, new_exp):
        self.exp = new_exp

    def tostring(self):
        print('''id:{} | name: {} | price: {} | import price: {}"
              \t\t\t\tquantity: {} | mfg: {} | exp: {}'''
              .format(self.id, self.name, self.price, self.import_price, self.quantity, self.mfg, self.exp))


class ItemInReceipt:
    item: Merchandise
    quantity: int  # số lượng bán
    sub_total: float  # thành tiền
    total: float  # thành tiền

    def __init__(self, item: Merchandise, quantity: int):
        self.item = item
        self.quantity = quantity
        self.sub_total = self.item.price
        self.total = self.sub_total * quantity


class Receipt:
    items: list[ItemInReceipt]
    id: int
    invoice_date: datetime.datetime

    def __init__(self, cart: list[ItemInReceipt]):
        self.items = cart
        self.id = random.randint(1, 9999)
        self.invoice_date = datetime.datetime.today()

    def total(self) -> float:
        return sum([x.total for x in self.items], 0)
