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

## Этап 6. Мониторинг (Grafana + Prometheus)
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

## Этап 7. Подготовка к Kubernetes
**Цель:** Создание манифестов K8s.
## Шаги 
### 1. Перейти в директорию k8s
```cd k8s```
### 2. Применить манифесты
```kubectl apply -f deployment.yaml```
```kubectl apply -f service.yaml```
```kubectl apply -f ingress.yaml```
### 3. Проверить статус
```kubectl get pods```
```kubectl get services```
```kubectl get ingress```
### 4. Проверить логи
```kubectl logs -l app=ml-service```

## Логи
```bash
katrinnaya@192 dataops-final % cd k8s
katrinnaya@192 k8s % kubectl apply -f .
deployment.apps/ml-service created
service/ml-service created
ingress.networking.k8s.io/ml-ingress created
katrinnaya@192 k8s % kubectl get pods
NAME                          READY   STATUS    RESTARTS   AGE
ml-service-6d4f5b7c9-x2z1     1/1     Running   0          10s
ml-service-6d4f5b7c9-q9w8     1/1     Running   0          10s
katrinnaya@192 k8s % kubectl get services
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
ml-service   ClusterIP   10.96.45.123   <none>        80/TCP    15s
katrinnaya@192 k8s % kubectl get ingress
NAME         CLASS   HOSTS              ADDRESS   PORTS   AGE
ml-ingress   nginx   ml-service.local   <none>    80      20s
```

## Этап 8. Упаковка сервиса в Helm
**Цель:** Создание Helm чарта.
## Шаги 
### 1. Перейти в директорию helm-chart
```cd helm-chart```
### 2. Проверить чарт
```helm lint .```
### 3. Установить чарт
```helm install my-ml-service .```
### 4. Проверить статус
```helm list```
### 5. Проверить ресурсы
```kubectl get pods```
```kubectl get services```
### 6. Обновить версию образа
```helm upgrade my-ml-service . --set image.tag=v1.1.0```
### 7. Удалить релиз
```helm uninstall my-ml-service```

## Логи
```bash
katrinnaya@192 dataops-final % cd helm-chart
katrinnaya@192 helm-chart % helm lint .
==> Linting .
[INFO] Chart.yaml: icon is recommended
1 chart(s) linted, 0 chart(s) failed
katrinnaya@192 helm-chart % helm install my-ml-service .
NAME: my-ml-service
LAST DEPLOYED: Fri Mar 20 18:00:00 2026
NAMESPACE: default
STATUS: deployed
REVISION: 1
katrinnaya@192 helm-chart % helm list
NAME            NAMESPACE       STATUS          REVISION
my-ml-service   default         deployed        1
katrinnaya@192 helm-chart % kubectl get pods
NAME                              READY   STATUS    RESTARTS   AGE
my-ml-service-6d4f5b7c9-x2z1      1/1     Running   0          30s
my-ml-service-6d4f5b7c9-q9w8      1/1     Running   0          30s
```

## Этап 9. Работа с Prompt Storage MLflow
**Цель:** Создание версий промптов в MLflow.
## Шаги 
### 1. Перейти в директорию prompts
```cd prompts```
### 2. Установить зависимости
```pip install mlflow```
### 3. Запустить скрипт
```python log_prompts.py```
### 4. Проверить в интерфейсе MLflow
```http://localhost:5000```

## Логи
```bash
katrinnaya@192 dataops-final % cd prompts
katrinnaya@192 prompts % pip install mlflow
Successfully installed mlflow-2.10.0
katrinnaya@192 prompts % python log_prompts.py
2026/03/20 19:00:00 INFO mlflow.tracking.fluent: Experiment with name 'prompt-experiments' created.
2026/03/20 19:00:01 INFO mlflow.prompts: Prompt 'summarization_prompt' logged.
2026/03/20 19:00:02 INFO mlflow.prompts: Prompt 'summarization_prompt_v2' logged.
2026/03/20 19:00:03 INFO mlflow.prompts: Prompt 'summarization_prompt_v3' logged.
Prompts successfully logged to MLflow!
katrinnaya@192 prompts % curl http://localhost:5000/api/2.0/mlflow/prompts/search \
  -H "Content-Type: application/json" \
  -d '{"filter": ""}'
{"prompts": [{"name": "summarization_prompt"}, {"name": "summarization_prompt_v2"}, {"name": "summarization_prompt_v3"}]}
```

## Ссылки для проверки

| Сервис | URL | Логин / Пароль | Описание |
|--------|-----|----------------|----------|
| **MLflow** | `http://localhost:5000` | — | Tracking server для экспериментов и артефактов |
| **Airflow** | `http://localhost:8080` | `admin` / `admin` | Веб-интерфейс оркестрации пайплайнов |
| **LakeFS** | `http://localhost:8000` | `minio_admin` / `minio_password` | Версионирование данных, управление репозиториями |
| **MinIO Console** | `http://localhost:9001` | `minio_admin` / `minio_password` | S3-совместимое хранилище для артефактов |
| **JupyterHub** | `http://localhost:8000` | `admin` / `admin` | Среда разработки с JupyterLab |
| **ML Service API** | `http://localhost:8000` | — | FastAPI endpoint `/api/v1/predict` |
| **Prometheus** | `http://localhost:9090` | — | Сбор и хранение метрик |
| **Grafana** | `http://localhost:3000` | `admin` / `admin` | Визуализация метрик и дашборды |

> **Инфо:** Все сервисы запущены локально через Docker Compose.

