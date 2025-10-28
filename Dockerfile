FROM python:3.11-slim

WORKDIR /app

# (opciono) sistemski alati ako želiš curl za healthcheck:
# RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8080
ENV PYTHONUNBUFFERED=1

# app.py sadrži WSGI objekat "app"
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
