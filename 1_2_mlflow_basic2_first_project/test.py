import mlflow.pyfunc
import pandas as pd
from sklearn.datasets import load_iris

# Tải lại data để test
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

# Gán đúng run_id hoặc lấy từ MLflow UI
logged_model_uri = "runs:/3181c6db25b4418f9213c25760a64e21/model"  # thay <run_id> bằng mã thật từ MLflow UI

# Load mô hình từ run đã log
loaded_model = mlflow.pyfunc.load_model(logged_model_uri)

# Dự đoán
predictions = loaded_model.predict(X)

# In kết quả
print(predictions[:5])
