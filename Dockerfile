FROM python:3.12-slim

ARG APP_VERSION=1.0.0
ENV APP_VERSION=${APP_VERSION}
ENV APP_ENVIRONMENT=dev
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app.main:app"]
