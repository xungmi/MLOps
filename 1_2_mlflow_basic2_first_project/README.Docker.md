# Mục tiêu
Học triển khai mô hình end-to-end tích hợp MLflow để tracking params, metri; quản lý mô hình và version

 # Công cụ
- IDE: VSCode
- Thư viện: pandas, numpy, scikit-learn, mlflow
- Dữ liệu: sử dụng dataset Iris từ sklearn.datasets

# Giải thích 1 số lệnh

1. mlflow run . -P penalty=l2 -P solver=lbfgs
    - Cách hoạt động:
        - MLflow tìm file MLproject trong thư mục hiện tại (.).
        - Đọc entry_points trong file MLproject → tìm main entry point.
        - Lấy các parameter (penalty, solver) từ dòng lệnh.
        - Dịch command: trong MLproject:
            - command: >
                - python train.py --penalty {penalty} --solver {solver}
                - Ta được: python train.py --penalty l2 --solver lbfgs
        - Ghi lại params, metrics, và model artifact vào thư mục mlruns/.

| Thành phần        | Ý nghĩa                                                                          |
| ----------------- | -------------------------------------------------------------------------------- |
| `mlflow run`      | Gọi MLflow để chạy một **project MLflow**.                                       |
| `.`               | Chạy project tại **thư mục hiện tại** (tức là nơi chứa file `MLproject`).        |
| `-P penalty=l2`   | Truyền **tham số penalty = l2** vào project (được định nghĩa trong `MLproject`). |
| `-P solver=lbfgs` | Truyền **tham số solver = lbfgs** vào script Python (thông qua entry point).     |