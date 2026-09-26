FROM python:3.11-slim 

WORKDIR /app

COPY auditor.py .
COPY modular_auditor.py .
COPY persistent_auditor.py .

CMD ["python", "persistent_auditor.py"]