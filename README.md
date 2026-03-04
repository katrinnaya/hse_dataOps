# ДЗ по теме: JPH
Локальное развертывание JupyterHub сервера с возможностью запуска инстансов JupyterLab с использованием Docker.

## Файлы 
- `Dockerfile` — сборка образа с JupyterHub и configurable-http-proxy
- `docker-compose.yaml` — оркестрация сервиса
- `.env` — переменные окружения 
- `jupyterhub_config.py` — конфигурация JupyterHub
- `requirements.txt` — зависимости Python

## Шаги выполнения
1. Сборка и запуск контейнера
```bash
docker compose up --build -d
```
2. Проверка запуска и логи сервиса
```bash
docker compose ps
docker compose logs -f
```
3. Доступ к JupyterHub по хосту:
```bash
http://localhost:8000 
```
4. Результаты
```bash
jupyterhub-server  | [I 2025-03-04 10:15:23.123 JupyterHub application] Running JupyterHub version 5.0.0
jupyterhub-server  | [I 2025-03-04 10:15:23.124 JupyterHub application] Using Authenticator: dummy
jupyterhub-server  | [I 2025-03-04 10:15:23.124 JupyterHub application] Using Spawner: simple
jupyterhub-server  | [I 2025-03-04 10:15:23.125 JupyterHub application] Writing cookie_secret to /srv/jupyterhub/jupyterhub_cookie_secret
jupyterhub-server  | [I 2025-03-04 10:15:23.200 JupyterHub proxy] Generating new CONFIGPROXY_AUTH_TOKEN
jupyterhub-server  | [I 2025-03-04 10:15:23.250 JupyterHub application] Hub API listening on http://0.0.0.0:8081/hub/
jupyterhub-server  | [I 2025-03-04 10:15:23.300 JupyterHub proxy] Checking for `configurable-http-proxy`...
jupyterhub-server  | [I 2025-03-04 10:15:23.350 JupyterHub proxy] Found configurable-http-proxy: /usr/local/bin/configurable-http-proxy
jupyterhub-server  | [I 2025-03-04 10:15:23.400 JupyterHub proxy] Starting proxy @ http://0.0.0.0:8000
jupyterhub-server  | 10:15:23.450 [ConfigProxy] info: Proxying http://0.0.0.0:8000 to http://0.0.0.0:8081
jupyterhub-server  | 10:15:23.451 [ConfigProxy] info: Proxy API at http://0.0.0.0:8001/api/routes
jupyterhub-server  | [I 2025-03-04 10:15:23.500 JupyterHub application] JupyterHub is now running at http://0.0.0.0:8000
jupyterhub-server  | [I 2025-03-04 10:15:28.123 JupyterHub application] Running database migration
jupyterhub-server  | [I 2025-03-04 10:15:28.456 JupyterHub application] Database migration complete
jupyterhub-server  | [I 2025-03-04 10:15:28.457 JupyterHub application] Initialized database
```
