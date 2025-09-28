import csv
from collections import defaultdict

# Bước 1: Đọc dữ liệu từ orders.csv
orders = []
with open("orders.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        orders.append(row)

# Bước 2: Lọc đơn hàng có status = completed
completed_orders = [o for o in orders if o["status"] == "completed"]

# Bước 3: Tính tổng amount theo ngày
amount_per_day = defaultdict(int)
for order in completed_orders:
    date = order["order_date"]
    amount = int(order["amount"])
    amount_per_day[date] += amount

# Bước 4: Ghi kết quả ra report.csv
with open("report.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["date", "amount"])
    for date, amount in sorted(amount_per_day.items()):
        writer.writerow([date, amount])

print("✅ File report.csv đã được xuất thành công!")
