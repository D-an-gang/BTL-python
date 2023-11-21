import datetime
import random
import CustomError
from MerchandiseEntity import Merchandise, Receipt, ItemInReceipt
from ManageProduct import ManageProduct


def convert_date(date_components: list[str]):
    if len(date_components) != 3:
        raise ValueError
    year, month, day = [int(item) for item in date_components]
    d = datetime.date(year, month, day)
    return d


def input_date() -> datetime.date:
    date_components = input('Nhập ngày theo định dạng YYYY-MM-DD: ').split('-')
    if len(date_components) != 3:
        raise ValueError
    year, month, day = [int(item) for item in date_components]
    d = datetime.date(year, month, day)
    return d


def option_1(db: ManageProduct):
    try:
        try:
            item: Merchandise = Merchandise()
            item.set_id(random.randint(0, 9999))
            item.set_name(input("Nhập tên sản phẩm: "))
            item.set_import_price(float(input("Nhập giá nhập hàng: ")))
            item.set_price(float(input("Nhập giá bán sản phẩm")))
            item.set_quantity(int(input("Nhập số lượng nhập hàng")))
            print("Nhập ngày sản xuất hàng hóa")
            item.set_mfg(input_date())
            print("Nhập hạn sử dụng hàng hóa")
            item.set_exp(input_date())
            db.add_merchandise(item)
        except ValueError:
            print('Nhập sai dữ liệu rồi 😭')
            print("Thêm hàng hóa thất bại")
    except CustomError.ModificationError:
        pass


def option_2(db: ManageProduct):
    mode: str = input("Lựa chọn chế độ tìm kiếm id | name | both (cả hai)")
    try:
        key: str = input("Nhập từ khóa tìm kiếm")
        res: list[Merchandise] = db.find_merchandise(key, mode)
        if len(res) <= 0:
            print("Không tìm thấy mặt hàng yêu cầu")
            return
        for x in res:
            print("Danh sách tìm kiếm")
            print("---------------------------------")
            x.tostring()
        print("---------------------------------")
        return
    except CustomError.OptionInvalidError as e:
        print(e.message)
    pass


def option_3(db: ManageProduct):
    try:
        db.display()
        id_target: int = int(input("Nhập id mặt hàng cần sửa: "))
        item: Merchandise = db.get_merchandise(id_target)
        if item is None:
            print("Không tìm thấy mặt hàng cần sửa")
            return
        input_1 = input("Nhập tên sản phẩm: (Không viết gì và Enter để bỏ qua)")
        if len(input_1) > 0:
            item.set_name(input_1)

        input_2 = input("Nhập giá nhập hàng: (Không viết gì và Enter để bỏ qua)")
        if len(input_2) > 0:
            item.set_import_price(float(input_2))

        input_3 = input("Nhập giá bán sản phẩm (Không viết gì và Enter để bỏ qua)")
        if len(input_3) > 0:
            item.set_price(float(input_3))

        input_4 = input("Nhập số lượng nhập hàng (Không viết gì và Enter để bỏ qua)")
        if len(input_4) > 0:
            item.set_quantity(int(input_4))

        input_5 = input("Nhập ngày sản xuất hàng hóa (Không viết gì và Enter để bỏ qua)")
        if len(input_5) > 0:
            item.set_mfg(convert_date(input_5.split('-')))
        input_6 = input("Nhập hạn sử dụng hàng hóa (Không viết gì và Enter để bỏ qua)")
        if len(input_6) > 0:
            item.set_exp(input_6.split('-'))
        try:
            db.update_merchandise(id_target, item)
        except CustomError.InvalidOperation as e:
            print("LỖI: KHÔNG THỂ CẬP NHẬT THÔNG TIN")
            print(e.message)
            return
    except ValueError:
        print('Nhập sai dữ liệu rồi 😭')


def option_4(db: ManageProduct):
    mode = input("Nhập chế độ sắp xếp: ASC - tăng dần | DES - giảm dần")
    try:
        res: list[tuple[Merchandise, float]] = db.sort_total_revenue(mode)
        for x in res:
            x[0].tostring()
            print(f"------->SALES: {x[1]}")
    except CustomError.OptionInvalidError as e:
        print(e.message)
        return


def option_5(db: ManageProduct):
    try:
        m: int = int(input("Nhập tháng cần hiển thị"))
        y: int = int(input("Nhập năm cần hiển thị"))
        src = db.total_daily_revenue(m, y)
        for x in src:
            print(f"Date:{x} ---> sale: {src[x]}")
    except ValueError:
        print("Dữ liệu nhập vào không đúng định dạng")
        return


def option_6(db: ManageProduct):
    db.display_top_5()


def option_7(db: ManageProduct):
    print("--------------------------------------")
    for x in db.close_to_exp():
        x.tostring()
    print("--------------------------------------")
    choice = input("Bạn có muốn điều chỉnh giá (Y/N)  ")
    choices = ["y", "n"]
    if choice.lower() not in choices:
        print("lựa chọn không hợp lệ, vui lòng thử lại sau.....")
        return
    if choice.lower() == "y":
        db.price_modify()
    return


def option_8(db: ManageProduct):
    cart: list[ItemInReceipt] = []
    print("--------------BÁN HÀNG----------------")
    print("Vui long lựa chọn sản phẩm:")
    db.display()
    try:
        while True:
            choice = input("\n Lựa chọn: (id sản phẩm cần bán) - Không nhập gì và Enter để xong lựa chọn ")
            if len(choice) <= 0:
                break
            target = int()
            item: Merchandise | None = db.get_merchandise(target)
            if item is None:
                print("Không tìm thấy sản phẩm!")
                return
            quan = int(input("Nhập số lượng cần bán"))
            cart.append(ItemInReceipt(item, quan))

        confirm = input("Xác nhận bán các sản phẩm trong giỏ hàng? (Y/N)  ")
        choices = ["y", "n"]
        if confirm.lower() not in choices:
            print("lựa chọn không hợp lệ, vui lòng thử lại sau.....")
            return
        if confirm.lower() == "y":
            db.add_invoice(cart)
    except ValueError:
        print("dự liệu nhập không hợp lệ, vui lòng thử lại sau")
    return


def option_9(db: ManageProduct):
    print("--------------------------------------")
    db.display()
    print("--------------------------------------")
    try:
        target: int = int(input("Nhập sản phẩm muốn xóa: "))
        if db.get_merchandise(target) is None:
            print("Không tìm thấy sản phẩm")
            return
        confirm = input("Xác nhận xóa sản phẩm? (Y/N)  ")
        choices = ["y", "n"]
        if confirm.lower() not in choices:
            print("lựa chọn không hợp lệ, vui lòng thử lại sau.....")
            return
        if confirm.lower() == "y":
            db.remove_merchandise(target)
            return
    except ValueError:
        print("Dữ liệu nhập vào không đúng")
        return
