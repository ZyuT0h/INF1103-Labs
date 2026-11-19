FROM python:3.11-slim

WORKDIR /app

COPY "lab9/main.py" .
COPY "lab9/inventory.json" .

CMD ["python", "lab9/main.py"]