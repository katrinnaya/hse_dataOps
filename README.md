# Домашнее задание по теме: Airflow в k8s
### Развертывание Airflow
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
