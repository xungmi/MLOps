# Khi chạy lệnh này, cần run app trước
curl -X POST http://localhost:5001/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [8.32, 41.0, 6.98, 1.02, 1.02, 2.62, 37.88, -122.23]}'