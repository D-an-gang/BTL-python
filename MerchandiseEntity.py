import datetime


class Merchandise:
    id: int
    name: str
    price: float
    import_price: float  # giá nhập
    quantity: int
    mfg: datetime  # ngày sản xuất
    exp: datetime  # hạn sử dụng

    def __init__(self):
        pass

    def __init__(self, code: int, name: str, price: float, ip: float, quan: int, mfg: datetime, exp: datetime):
        self.id = code
        self.name = name
        self.price = price
        self.import_price = ip
        self.quantity = quan
        self.mfg = mfg
        self.exp = exp

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
    invoice_date: datetime
