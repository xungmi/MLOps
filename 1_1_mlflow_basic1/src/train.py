import mlflow
import logging
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("mlops.log"),
        logging.StreamHandler()
    ]
)

logging.info("Loading data...")
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)
logging.info("Data loaded and split.")

logging.info("Training model...")
with mlflow.start_run():
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)

    logging.info("Model training complete.")
    logging.info(f"Model Accuracy: {acc:.4f}")
    mlflow.log_metric("accuracy", acc)
