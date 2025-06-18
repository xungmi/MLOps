# Base image: sử dụng Python 3.9 slim để nhẹ và nhanh
FROM python:3.9-slim

# Thiết lập thư mục làm việc trong container
WORKDIR /app

RUN apt-get update && apt-get install -y git

# Copy file requirements.txt vào container
COPY requirements.txt .

# Cài đặt các dependencies từ requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn dự án vào container
COPY . .

# Lệnh chạy mặc định khi container khởi động: chạy file train.py
CMD ["python", "src/train.py"]
