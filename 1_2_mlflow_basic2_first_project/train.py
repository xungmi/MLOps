import argparse
import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from mlflow.models.signature import infer_signature
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def main(penalty: str, solver: str):
    # Load data
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Log parameters
    mlflow.log_param("penalty", penalty)
    mlflow.log_param("solver", solver)

    # Train model
    model = LogisticRegression(penalty=penalty, solver=solver, max_iter=200)
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    # Log metrics
    mlflow.log_metric("accuracy", acc)

    # Log model with signature để MLflow biết được input/output của 
    # mô hình để phục vụ tái sử dụng/deployment.
    signature = infer_signature(X_train, model.predict(X_train))
    mlflow.sklearn.log_model(model, "model", signature=signature,  
                            input_example=X_train,
                            registered_model_name="tracking-quickstart")

    # Optional: add tag
    mlflow.set_tag("description", "Logistic Regression on Iris dataset")

    print(f"Trained and logged model with accuracy: {acc:.4f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--penalty", type=str, default="l2")
    parser.add_argument("--solver", type=str, default="lbfgs")
    args = parser.parse_args()
    main(args.penalty, args.solver)
