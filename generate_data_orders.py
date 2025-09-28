import csv
from datetime import datetime, timedelta
import random

# Cấu trúc file CSV
header = ["order_id", "order_date", "customer_id", "amount", "status"]

# Sinh dữ liệu giả lập
statuses = ["completed", "pending", "cancelled"]
start_date = datetime(2025, 9, 1)

rows = []
order_id = 1
for day in range(10):  # 5 ngày dữ liệu
    order_date = (start_date + timedelta(days=day)).strftime("%Y-%m-%d")
    for _ in range(random.randint(3, 6)):  # mỗi ngày 3-6 đơn hàng
        customer_id = random.randint(1001, 1010)
        amount = random.randint(50, 500)
        status = random.choice(statuses)
        rows.append([order_id, order_date, customer_id, amount, status])
        order_id += 1

# Ghi ra file CSV
with open("orders.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print("✅ File orders.csv đã được tạo thành công!")
