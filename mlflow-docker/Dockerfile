FROM python:3.11-slim

# Установка зависимостей
RUN pip install --no-cache-dir mlflow psycopg2-binary

# Создание директории для артефактов
WORKDIR /mlflow
RUN mkdir -p /mlflow/artifacts

# Порт MLflow сервера
EXPOSE 5000

# Команда по умолчанию (переопределяется в docker-compose)
CMD ["mlflow", "server", "--host", "0.0.0.0", "--port", "5000"]
