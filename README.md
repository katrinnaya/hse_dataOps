# Домашнее задание по теме: DVC
### Развертывание LakeFS
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
