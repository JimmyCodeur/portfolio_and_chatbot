FROM python:3.11-slim

WORKDIR /app

COPY ../front /app

EXPOSE 8011

CMD ["python", "-m", "http.server", "8011"]
