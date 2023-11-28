import datetime

from MerchandiseEntity import Merchandise, ItemInReceipt, Receipt, receiptwithdate

merchandise_list: list[Merchandise] = [
    Merchandise("Smartphone Pro X", 1200.0, 900.0, 50, datetime.date(2023, 1, 1), datetime.date(2023, 12, 31)),
    Merchandise("Laptop Ultra Y", 1800.0, 1500.0, 30, datetime.date(2023, 2, 1), datetime.date(2023, 12, 15)),
    Merchandise("Smartwatch Advanced Z", 500.0, 400.0, 40, datetime.date(2023, 3, 1), datetime.date(2023, 12, 10)),
    Merchandise("Gaming Console Elite", 600.0, 550.0, 20, datetime.date(2023, 4, 1), datetime.date(2023, 11, 30)),
    Merchandise("Wireless Earbuds Pro", 150.0, 120.0, 60, datetime.date(2023, 5, 1), datetime.date(2023, 12, 20)),
    Merchandise("4K Smart TV Masterpiece", 2000.0, 1800.0, 15, datetime.date(2023, 6, 1), datetime.date(2023, 11, 15)),
    Merchandise("High-Performance Blender", 120.0, 100.0, 35, datetime.date(2023, 7, 1), datetime.date(2023, 12, 5)),
    Merchandise("Digital Camera Pro-shot", 800.0, 700.0, 25, datetime.date(2023, 8, 1), datetime.date(2023, 11, 25)),
    Merchandise("Home Security System", 350.0, 280.0, 45, datetime.date(2023, 9, 1), datetime.date(2023, 12, 8)),
    Merchandise("Fitness Tracker UltraFit", 200.0, 180.0, 18, datetime.date(2023, 10, 1), datetime.date(2023, 11, 20))
]

cart: list[ItemInReceipt] = [
    ItemInReceipt(merchandise_list[0], 10),
    ItemInReceipt(merchandise_list[1], 9),
    ItemInReceipt(merchandise_list[2], 5),
    ItemInReceipt(merchandise_list[3], 11),
    ItemInReceipt(merchandise_list[4], 10),
    ItemInReceipt(merchandise_list[5], 2),
    ItemInReceipt(merchandise_list[6], 12),
    ItemInReceipt(merchandise_list[7], 1),
    ItemInReceipt(merchandise_list[8], 7),
    ItemInReceipt(merchandise_list[9], 3),
]

start_date = datetime.datetime(2023, 1, 1)
date_objects = [start_date + datetime.timedelta(days=i * 30) for i in range(10)]

invoices: list[Receipt] = [
    Receipt(cart[3: 5]),
    receiptwithdate(cart[0: 7], date_objects[0]),
    receiptwithdate(cart[2: 3], date_objects[1]),
    receiptwithdate(cart[1: 6], date_objects[3]),
    Receipt(cart[4: 7]),
]
