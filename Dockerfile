FROM python:3.11-slim

WORKDIR /app

COPY lab8_inventory.py .
COPY inventory.json .

CMD ["python", "lab8_inventory.py"]