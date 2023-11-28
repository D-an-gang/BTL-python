import Functions as fn
import MockData
from ManageProduct import ManageProduct

menu: str = '''
    ----STORE MANAGEMENT -----
    1.Thêm hàng hóa
    2.Tìm kiếm hàng hóa
    3.Sửa thông tin hàng hóa
    4.Sắp xếp theo doanh thu hàng hóa
    5.Thống kê doanh thu theo ngày của cửa hàng
    6.Thống kê top hàng hóa doanh thu cao, thấp nhất
    7.Hiển thị hàng hóa sắp hết hạn
    8.Bán hàng
    9.Xóa hàng hóa
    10.Thoát chương trình
'''
# Khởi tạo quản lý cửa hàng
db: ManageProduct = ManageProduct()
db.stock = MockData.merchandise_list
db.invoices = MockData.invoices
while True:
    print(menu)
    try:
        choice = int(input("Type in corresponding number to select: "))
    except ValueError:
        choice = int(input("Input must be number -_- : "))
    match choice:
        case 1:
            fn.option_1(db)
        case 2:
            fn.option_2(db)
        case 3:
            fn.option_3(db)
        case 4:
            fn.option_4(db)
        case 5:
            fn.option_5(db)
        case 6:
            fn.option_6(db)
        case 7:
            fn.option_7(db)
        case 8:
            fn.option_8(db)
        case 9:
            fn.option_9(db)
        case 10:
            print("Exiting...")
            exit(0)
        # hidden option 👀
        case 22:
            db.display()
        case _:
            print(menu)
            pass
