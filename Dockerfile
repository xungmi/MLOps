# Base image: sử dụng Python 3.9 slim để nhẹ và nhanh
FROM python:3.9-slim

# Install curl and other dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    bash \
    apt-transport-https \
    ca-certificates \
    gnupg \
    lsb-release && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Cài kubectl (latest stable)
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" \
    && install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl \
    && rm kubectl

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Copy file requirements.txt vào container
COPY requirements.txt .

# Cài đặt các dependencies từ requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn dự án vào container
COPY . .

EXPOSE 5001

# Lệnh chạy mặc định khi container khởi động: chạy file train.py
CMD ["python", "src/train.py"]
