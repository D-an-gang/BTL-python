import datetime

import Functions as fn
from ManageProduct import ManageProduct
from MerchandiseEntity import Merchandise

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
merchandise_list: list[Merchandise] = [
    Merchandise("Smartphone Pro X", 1200.0, 900.0, 50, datetime.date(2023, 1, 1), datetime.date(2023, 12, 31)),
    Merchandise("Laptop Ultra Y", 1800.0, 1500.0, 30, datetime.date(2023, 2, 1), datetime.date(2023, 12, 15)),
    Merchandise("Smartwatch Advanced Z", 500.0, 400.0, 40, datetime.date(2023, 3, 1), datetime.date(2023, 12, 10)),
    Merchandise("Gaming Console Elite", 600.0, 550.0, 20, datetime.date(2023, 4, 1), datetime.date(2023, 11, 30)),
    Merchandise("Wireless Earbuds Pro", 150.0, 120.0, 60, datetime.date(2023, 5, 1), datetime.date(2023, 12, 20)),
    Merchandise("4K Smart TV Masterpiece", 2000.0, 1800.0, 15, datetime.date(2023, 6, 1), datetime.date(2023, 11, 15)),
    Merchandise("High-Performance Blender", 120.0, 100.0, 35, datetime.date(2023, 7, 1), datetime.date(2023, 12, 5)),
    Merchandise("Digital Camera Proshot", 800.0, 700.0, 25, datetime.date(2023, 8, 1), datetime.date(2023, 11, 25)),
    Merchandise("Home Security System", 350.0, 280.0, 45, datetime.date(2023, 9, 1), datetime.date(2023, 12, 8)),
    Merchandise("Fitness Tracker UltraFit", 200.0, 180.0, 18, datetime.date(2023, 10, 1), datetime.date(2023, 11, 20))
]
db.stock = merchandise_list
isFinish = False
while not isFinish:
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
