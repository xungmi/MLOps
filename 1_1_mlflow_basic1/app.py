# Flask: Framework nhẹ để tạo REST API
# request: Lấy dữ liệu từ POST request
# jsonify: Trả kết quả dạng JSON
# joblib: Để load model đã lưu
# numpy: Xử lý input dạng mảng
from flask import Flask, request, jsonify
import joblib
import numpy as np

model = joblib.load("model.pkl")
app = Flask(__name__) # cho phép Flask xác định thư mục hiện tại để tìm templates/static nếu có

@app.route("/predict", methods=["POST"])
def predict():
    input_data = request.get_json()
    features = np.array(input_data["features"]).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)