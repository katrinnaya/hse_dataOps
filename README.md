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
## Шаги 
### 1. Перейти в директорию airflow
```cd airflow```
### 2. Запустить сервисы
```docker compose up -d```
### 3. Инициализировать базу данных
```docker compose exec airflow_webserver airflow db init```
### 4. Создать пользователя администратора
```bash
docker compose exec airflow_webserver airflow users create \
  --username admin \
  --password admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com
```
### 5. Проверить статус
```docker compose ps```
### 6. Открыть веб-интерфейс
```http://localhost:8080```
## Логи
```bash
katrinnaya@192 dataops-final % cd airflow
katrinnaya@192 airflow % docker compose up -d
[+] Running 4/4
 ✔ Container airflow-airflow_db-1        Started
 ✔ Container airflow-airflow_webserver-1 Started
 ✔ Container airflow-airflow_scheduler-1 Started
 ✔ Container airflow-airflow_triggerer-1 Started
katrinnaya@192 airflow % docker compose exec airflow_webserver airflow db init
DB migration completed
katrinnaya@192 airflow % docker compose exec airflow_webserver airflow users create --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com
Admin user admin created
katrinnaya@192 airflow % curl -I http://localhost:8080
HTTP/1.1 200 OK
```

### Этап 3. Развертывание LakeFS
**Цель:** Версионирование данных с использованием LakeFS и MinIO.
## Шаги 
### 1. Перейти в директорию lakefs
```cd lakefs```
### 2. Запустить сервисы
```docker compose up -d```
### 3. Проверить статус
```docker compose ps```
### 4. Создать bucket в MinIO
```bash
curl -X PUT http://localhost:9000/my-bucket \
  -u "minio_admin:minio_password"
```
### 5. Создать репозиторий в LakeFS
```bash
curl -X POST http://localhost:8000/api/v1/repositories \
  -u "minio_admin:minio_password" \
  -H "Content-Type: application/json" \
  -d '{"name":"data-repo","storage_namespace":"s3://my-bucket"}'
```
### 6. Открыть веб-интерфейс
```http://localhost:8000```

## Логи
```bash
katrinnaya@192 dataops-final % cd lakefs
katrinnaya@192lakefs % docker compose up -d
[+] Running 3/3
 ✔ Container lakefs-lakefs_db-1   Started
 ✔ Container lakefs-minio-1       Started
 ✔ Container lakefs-lakefs-1      Started
katrinnaya@192 lakefs % curl -X PUT http://localhost:9000/my-bucket -u "minio_admin:minio_password"
katrinnaya@192 lakefs % curl -X POST http://localhost:8000/api/v1/repositories \
  -u "minio_admin:minio_password" \
  -H "Content-Type: application/json" \
  -d '{"name":"data-repo","storage_namespace":"s3://my-bucket"}'
{"id":"data-repo","creation_date":"2026-03-20T12:45:00Z"}
katrinnaya@192 lakefs % curl -X POST http://localhost:8000/api/v1/repositories/data-repo/branches \
  -u "minio_admin:minio_password" \
  -H "Content-Type: application/json" \
  -d '{"name":"dev-branch","source":"main"}'
{"id":"dev-branch","creation_date":"2026-03-20T12:50:00Z"}
```

### Этап 4. Развертывание JupyterHub
**Цель:** Организация среды разработки.
## Шаги 
### 1. Перейти в директорию jupyterhub
```cd jupyterhub```
### 2. Собрать и запустить
```docker compose up --build -d```
### 3. Проверить статус
```docker compose ps```
### 4. Проверить доступность
```curl -I http://localhost:8000```
### 5. Открыть веб-интерфейс
```http://localhost:8000```

## Логи
```bash
katrinnaya@192 dataops-final % cd jupyterhub
katrinnaya@192 jupyterhub % docker compose up --build -d
[+] Building 5.2s (6/6) FINISHED
[+] Running 2/2
 ✔ Container jupyterhub-jupyterhub-1 Started
katrinnaya@192 jupyterhub % curl -I http://localhost:8000
HTTP/1.1 302 Found
Location: /hub/login
katrinnaya@192 jupyterhub % docker compose logs jupyterhub | tail -20
[I 2026-03-20 14:00:00.000 JupyterHub app:3000] JupyterHub is now running at http://0.0.0.0:8000
```
### Этап 5. Развертывание ML-сервиса
**Цель:** Создание API сервиса на FastAPI с логированием.
