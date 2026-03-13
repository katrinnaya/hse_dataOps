# ДЗ по теме 20: MLflow сервер с PostgreSQL и Docker

Разворачивание MLflow Tracking Server с использованием PostgreSQL как backend store и локальной файловой системы для артефактов.

## Состав

- `db` — PostgreSQL 15
- `mlflow` — MLflow Tracking Server на Python 3.11

## Запуск сервисов
```bash
docker-compose up -d
```
## Проверка логов
```bash
docker-compose logs -f
```
## MLflow UI
``` http://localhost:5000 ```
