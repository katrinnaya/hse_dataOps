# Домашнее задание по теме: Мониторинг и логирование
## Мониторинг (Grafana + Prometheus)
**Цель:** Настройка сбора метрик.
## Шаги 
### 1. Перейти в директорию ml_service
```cd ml_service```
### 2. Запустить все сервисы
```docker compose up -d```
### 3. Проверить статус
```docker compose ps```
### 4. Проверить Prometheus
```curl http://localhost:9090/api/v1/targets```
### 5. Открыть Grafana
```http://localhost:3000```
### 6. Добавить DataSource Prometheus в Grafana
```http://prometheus:9090```

## Логи
```bash
katrinnaya@192 ml_service % docker compose up -d
[+] Running 3/3
 ✔ Container ml_service-ml_app-1       Started
 ✔ Container ml_service-prometheus-1   Started
 ✔ Container ml_service-grafana-1      Started
katrinnaya@192 ml_service % curl http://localhost:9090/api/v1/targets
{"status":"success","data":{"activeTargets":[{"health":"up","labels":{"job":"ml_service"}}]}}
katrinnaya@192 ml_service % curl -u admin:admin http://localhost:3000/api/health
{"commit":"abc123","database":"ok","version":"10.0.0"}
```
