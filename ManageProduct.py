import CustomError
from MerchandiseEntity import Merchandise, ItemInReceipt, Receipt


class ManageProduct:
    invoices: list[Receipt]
    stock: list[Merchandise]

    def __init__(self):
        pass

    def add_merchandise(self, item: Merchandise) -> None:
        for x in self.stock:
            if item.id == x.id:
                raise CustomError.ModificationError(item.id)
            self.stock.append(item)

    def find_merchandise(self, search_key: str, opt: str) -> list[Merchandise]:
        available_opts = ["id", "name", "both"]
        res: list[Merchandise] = []
        if str.lower(opt) not in available_opts:
            raise CustomError.OptionInvalidError(available_opts)
        match opt:
            case "id":
                self.stock.sort(key=lambda x: x.id)
                res = [x for x in self.stock if search_key in str(x.id)]
            case "name":
                self.stock.sort(key=lambda x: x.name)
                res = [x for x in self.stock if search_key in x.name]
            case "both":
                self.stock.sort(key=lambda x: x.name or x.id)
                res = [x for x in self.stock if (search_key in x.name) or (search_key in x.id)]
        return res

    def daily_revenue_per_item(self, item: Merchandise):
        res: float = 0
        for x in self.invoices:
            for i in x.items:
                if item.id == i.item.id:
                    res = res + i.total
        return res


    def display(self):
        print("-------------------------------------------------")
        for x in self.stock:
            x.tostring()
        print("-------------------------------------------------")

