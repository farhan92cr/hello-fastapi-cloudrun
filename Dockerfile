# Stage 1 - Build
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2 - Runtime
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /usr/local /usr/local
COPY main.py .
USER nobody
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
