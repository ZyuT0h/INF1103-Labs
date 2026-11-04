FROM python:3.11-slim

WORKDIR /app

COPY "lab9/lab9_inheritance.py" .
COPY "lab9/inventory.json" .

CMD ["python", "lab9_inheritance.py"]