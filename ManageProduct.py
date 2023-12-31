import datetime

import CustomError
from MerchandiseEntity import Merchandise, Receipt, ItemInReceipt
from enum import Enum


class ManageProduct:
    invoices: list[Receipt]
    stock: list[Merchandise]

    def __init__(self):
        self.invoices = []
        self.stock = []

    def add_merchandise(self, item: Merchandise) -> None:
        """
        Thêm hàng hóa vào kho hàng
        :param item: object Merchandise
        """
        for x in self.stock:
            if item.id == x.id:
                raise CustomError.ModificationError(item.id)
        self.stock.append(item)

    def find_merchandise(self, search_key: str, opt: str) -> list[Merchandise]:
        """
        Tìm kiếm hàng hóa
        :param search_key: từ khóa tìm kiếm
        :param opt: id - name - both --> tìm kiếm theo id,tên hoặc cả 2
        :return:object Merchandise
        """
        available_opts = ["id", "name", "both"]
        search_key.lower()
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
                res = [x for x in self.stock if (search_key in x.name.lower()) or (search_key in str(x.id))]
        return res

    def daily_revenue_per_item(self, item: Merchandise):
        """
        tổng doanh thu theo ngày của từng mặt hàng
        :param item: mặt hàng cần xuất dữ liệu
        :return: float---kết quả
        """
        res: float = 0
        for x in self.invoices:
            for i in x.items:
                if item.id == i.item.id:
                    res = res + i.total
        return res

    def display(self):
        """
        Hiển thị danh sách hàng hóa
        """
        print("-------------------------------------------------")
        for x in self.stock:
            x.tostring()
        print("-------------------------------------------------")

    def total_daily_revenue(self, month: int, year: int) -> dict[datetime.date, float]:
        """
        Tính tổng doanh thu theo ngày
        :param month: số tháng
        :param year: số ngày
        :return: tổng doanh thu cửa hàng theo ngày -- kiểu float
        """
        res: dict[datetime.date, float] = {}
        try:
            for invoice in self.invoices:
                if year == invoice.invoice_date.year and month == invoice.invoice_date.month:
                    if invoice.invoice_date in res:
                        res[invoice.invoice_date] += invoice.total()
                    else:
                        res[invoice.invoice_date] = invoice.total()
            return res
        except TypeError:
            raise TypeError

    def sort_total_revenue(self, mode: str) -> list[tuple[Merchandise, float]] | None:
        """
        Sắp xếp doanh thu từng mặt hàng
        :param mode: 'asc' hoặc 'desc'
        :return: None nếu không có dữ liệu, list[tuple[Merchandise, float]] nếu sort thành công
        """
        available_opts: list[str] = ["asc", "desc"]
        if mode not in available_opts:
            raise CustomError.OptionInvalidError(available_opts)
        res: dict[Merchandise, float] = {}
        # output: list[tuple[Merchandise, float]] = []
        try:
            for invoice in self.invoices:
                for item in invoice.items:
                    if item.item not in res.keys():
                        res[item.item] = item.total
                    else:
                        res[item.item] += item.total
        except TypeError:
            raise TypeError
        if len(res) != 0:
            output = sorted(res.items(), key=lambda kv: (kv[1], kv[0]))
        else:
            return None
        match mode:
            case "asc":
                output = sorted(output, key=lambda x: x[1])
            case "desc":
                output = sorted(output, key=lambda x: x[1], reverse=True)
        return output

    def display_top_5(self):
        """
        Hiển thị 5 sản phẩm doanh thu cao nhất, 5 mặt hàng có doanh thu thấp nhất
        """
        try:
            col: list[tuple[Merchandise, float]] = self.sort_total_revenue("desc")
            print("Top sales:")
            for x in col[:5]:
                x[0].tostring()
                print("------->SALES: {0}".format(x[1]))
            print("---------------------------------------")
            print("Bottom 5")
            for x in col[-5:-1]:
                x[0].tostring()
                print("------->SALES: {0}".format(x[1]))
            print("---------------------------------------")
        except TypeError:
            raise TypeError

    def close_to_exp(self) -> list[Merchandise]:
        return [x for x in self.stock if (x.exp - datetime.date.today()).days <= 42]

    def price_modify(self) -> None:
        """
        Tổng hợp hàng hóa trong của hàng sắp hết hạn sử dụng, tính giá mới cho mặt hàng đó
        """

        class CalWeekRes(Enum):
            OUTDATED: int = -1
            LESS_3_WEEKS: int = 1
            MORE_3_WEEKS: int = 0
            DAYS_EXPS: int = 6
            WEEKS_3: int = 21
            WEEKS_6: int = 42
            DISCOUNT_M3W: float = 23.5
            DISCOUNT_L3W: float = 56.9

        def cal_week(time: datetime.date) -> CalWeekRes:
            if datetime.date.today() >= time:
                return CalWeekRes.OUTDATED
            else:
                if (time - datetime.date.today()).days < CalWeekRes.WEEKS_3.value:
                    return CalWeekRes.LESS_3_WEEKS
                if (time - datetime.date.today()).days >= CalWeekRes.WEEKS_3.value:
                    return CalWeekRes.MORE_3_WEEKS

        col: list[Merchandise] = self.close_to_exp()

        for item in col:
            match cal_week(item.exp):
                case CalWeekRes.OUTDATED:
                    # Xóa sạch số lượng nếu phát hiện quá hạn??? quantity -> 0
                    pass
                case CalWeekRes.LESS_3_WEEKS:
                    item.price /= ((100.0 - CalWeekRes.DISCOUNT_L3W.value) / 100)
                case CalWeekRes.MORE_3_WEEKS:
                    item.price *= ((100.0 - CalWeekRes.DISCOUNT_M3W.value) / 100)
                case _:
                    continue
        print("\033[1;32mĐiều chỉnh giá thành công\033[0m")
        self.display()
        return

    def update_merchandise(self, target_id: int, item: Merchandise) -> None:
        """
        Sửa thông tin hàng hóa
        :param target_id: id của item cần sửa
        :param item: obj Merchandise sau khi đã sửa
        :raise InvalidOperation khi sửa đổi id của item hoặc id của item không tồn tại
        """
        err_msg = ["Merchandise id not found", "U cannot change the merchandise id"]
        if target_id != item.id:
            raise CustomError.InvalidOperation(err_msg[1])
        if target_id not in [x.id for x in self.stock]:
            raise CustomError.InvalidOperation(err_msg[0])
        for x in self.stock:
            if x.id == target_id:
                x = item

    def remove_merchandise(self, target_id: int):
        filtered = [x for x in self.stock if x.id != target_id]
        self.stock = filtered

    def add_invoice(self, cart: list[ItemInReceipt]):
        for x in cart:
            buffer = next((item for item in self.stock if item.id == x.item.id), None)
            if buffer is not None:
                buffer.quantity -= x.quantity
        res: Receipt = Receipt(cart)
        self.invoices.append(res)

    def get_merchandise(self, id_moc: int):
        for x in self.stock:
            if x.id == id_moc:
                return x
        return None
