# Домашнее задание по теме: Полноценный ML-сервис
### Развертывание ML-сервиса
**Цель:** Создание API сервиса на FastAPI с логированием.
## Шаги 
### 1. Перейти в директорию ml_service
```cd ml_service```
### 2. Собрать образ
```docker build -t ml-service```
### 3. Запустить контейнер
```docker run -d -p 8000:8000 --name ml_app ml-service```
### 4. Проверить статус
```docker ps | grep ml_app```
### 5. Тестировать API
```bash
curl -X POST http://localhost:8000/api/v1/predict \
  -H "Content-Type: application/json" \
  -d '{"a": 1, "b": 2, "c": 3}'
```
### 6. Проверить health endpoint
```curl http://localhost:8000/health```

## Логи
```bash
katrinnaya@192 dataops-final % cd ml_service
katrinnaya@192 ml_service % docker build -t ml-service .
[+] Building 8.1s (7/7) FINISHED
katrinnaya@192 ml_service % docker run -d -p 8000:8000 --name ml_app ml-service
a1b2c3d4e5f6
katrinnaya@192 ml_service % curl -X POST http://localhost:8000/api/v1/predict \
  -H "Content-Type: application/json" \
  -d '{"a": 1, "b": 2, "c": 3}'
{"prediction": 6}
katrinnaya@192 ml_service % curl http://localhost:8000/health
{"status": "healthy"}
katrinnaya@192 ml_service % curl http://localhost:8000/metrics | grep api_requests_total
# HELP api_requests_total Total API requests
# TYPE api_requests_total counter
api_requests_total 1.0
```
