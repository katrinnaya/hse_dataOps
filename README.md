# Итоговое домашнее задание
## Описание проекта
Проект реализует полный цикл DataOps: от развертывания инфраструктуры (MLflow, Airflow, LakeFS, JupyterHub) до создания ML-сервиса, его мониторинга и подготовки к деплою в Kubernetes с использованием Helm.
## Этапы развертывания
### Этап 1. Развертывание MLflow
**Цель:** Развернуть сервер MLflow для трекинга экспериментов и хранения артефактов с использованием PostgreSQL.
## Шаги 
### 1. Перейти в директорию mlflow
```cd mlflow```
### 2. Запустить сервисы
```docker compose up --build -d```
### 3. Проверить статус контейнеров
```docker compose ps```
### 4. Проверить доступность MLflow
```curl http://localhost:5000/health```
### 5. Открыть веб-интерфейс и создать эксперимент
```http://localhost:5000```

## Логи
```bash
katrinnaya@192 dataops-final % cd mlflow
katrinnaya@192 % docker compose up --build -d
[+] Building 12.5s (8/8) FINISHED
[+] Running 3/3
 ✔ Network mlflow_default        Created
 ✔ Container mlflow-mlflow_db-1  Started
 ✔ Container mlflow-mlflow_server-1 Started
katrinnaya@192 mlflow % docker compose ps
NAME                     IMAGE          COMMAND                  SERVICE        STATUS          PORTS
mlflow-mlflow_db-1       postgres:15    "docker-entrypoint.s…"   mlflow_db      Up (healthy)    0.0.0.0:5432->5432/tcp
mlflow-mlflow_server-1   mlflow-mlflow  "mlflow server --hos…"   mlflow_server  Up              0.0.0.0:5000->5000/tcp
katrinnaya@192 mlflow % curl http://localhost:5000/health
{"status": "OK"}
```
### Этап 2. Развертывание Airflow
**Цель:** Развернуть Airflow для оркестрации пайплайнов.

