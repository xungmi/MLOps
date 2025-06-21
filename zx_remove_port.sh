#!/bin/bash
PORT=5000

echo "Đang tìm các tiến trình đang LISTEN trên cổng $PORT..."

lsof -nP -iTCP:$PORT -sTCP:LISTEN

PIDS=$(lsof -nP -iTCP:$PORT -sTCP:LISTEN | awk 'NR>1 {print $2}' | sort -u)

if [ -n "$PIDS" ]; then
    echo "Các PID đang chiếm cổng $PORT:"
    echo "$PIDS"
    echo "Thực hiện kill -9 từng PID..."

    # Cách 1: dùng vòng lặp
    for pid in $PIDS; do
        kill -9 $pid && echo "Đã kill PID $pid"
    done

    echo "Đã giải phóng cổng $PORT."
else
    echo "Không có tiến trình nào chiếm cổng $PORT."
fi
