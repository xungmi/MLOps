#!/bin/bash

# Dừng script nếu có lỗi
set -e

# Tên experiment bạn muốn sử dụng
EXPERIMENT_NAME="test2"

# Các tham số cho model
PENALTY="l2"
SOLVER="lbfgs"

# Gọi mlflow run
mlflow run . \
  --env-manager=local \
  --experiment-name "$EXPERIMENT_NAME" \
  -P penalty="$PENALTY" \
  -P solver="$SOLVER"