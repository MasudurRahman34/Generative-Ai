FROM python:3.12

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# 4. Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app
COPY data/ ./data

# 6. Default command (console test for now)
CMD ["python", "app/main.py"]