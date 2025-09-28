# Bài 2 - Bài tập kỹ thuật

Bao gồm các script Python để sinh dữ liệu đơn hàng giả lập và cho ra kết quả doanh thu theo từng ngày

## Cấu trúc thư mục

```
├── generate_data_orders.py    # Script sinh dữ liệu đơn hàng giả lập
├── aggregate_orders.py        # Script phân tích và tạo báo cáo
├── orders.csv                 # File dữ liệu đơn hàng
├── report.csv                 # File báo cáo doanh thu theo ngày
└── README.md                  # Tài liệu hướng dẫn
```

## Chi tiết

### 1. Sinh dữ liệu đơn hàng (`generate_data_orders.py`)
- Tạo dữ liệu đơn hàng giả lập cho 10 ngày
- Mỗi ngày có 3-6 đơn hàng ngẫu nhiên
- Dữ liệu bao gồm:
  - `order_id`: ID đơn hàng
  - `order_date`: Ngày đặt hàng
  - `customer_id`: ID khách hàng (1001-1010)
  - `amount`: Giá trị đơn hàng (50-500)
  - `status`: Trạng thái đơn hàng (completed, pending, cancelled)

### 2. Phân tích dữ liệu (`aggregate_orders.py`)
- Đọc dữ liệu từ file `orders.csv`
- Lọc các đơn hàng có trạng thái "completed"
- Tính tổng doanh thu theo từng ngày
- Xuất báo cáo ra file `report.csv`

## Cách sử dụng

### Bước 1: Sinh dữ liệu
```bash
python generate_data_orders.py
```
✅ Kết quả: File `orders.csv` được tạo với dữ liệu đơn hàng giả lập

### Bước 2: Tạo báo cáo
```bash
python aggregate_orders.py
```
✅ Kết quả: File `report.csv` được tạo với báo cáo doanh thu theo ngày

## Định dạng dữ liệu

### File orders.csv
```csv
order_id,order_date,customer_id,amount,status
1,2025-09-01,1006,469,cancelled
2,2025-09-01,1002,58,pending
3,2025-09-01,1003,96,completed
...
```

### File report.csv
```csv
date,amount
2025-09-01,96
2025-09-02,207
2025-09-03,473
...
```

## Yêu cầu hệ thống
- Python 3.x
- Các thư viện chuẩn: `csv`, `datetime`, `collections`, `random`

