# Конфигурационный файл JupyterHub

import os
from jupyterhub.auth import DummyAuthenticator
from jupyterhub.spawner import SimpleLocalProcessSpawner

# Настройки безопасности
c.JupyterHub.port = int(os.getenv('JUPYTERHUB_PORT', 8000))
c.JupyterHub.ip = os.getenv('JUPYTERHUB_HOST', '0.0.0.0')
c.JupyterHub.hub_ip = '0.0.0.0'

# Настройки аутентификации (для разработки используем DummyAuthenticator)
c.JupyterHub.authenticator_class = DummyAuthenticator
c.DummyAuthenticator.password = os.getenv('JUPYTERHUB_ADMIN_PASSWORD', 'admin')

# Настройки spawner (запуск пользовательских серверов)
c.JupyterHub.spawner_class = SimpleLocalProcessSpawner
c.SimpleLocalProcessSpawner.home_dir = '/srv/jupyterhub/data'

# Настройки администратора
admin_users = set()
admin = os.getenv('JUPYTERHUB_ADMIN', 'admin')
if admin:
    admin_users.add(admin)
c.Authenticator.admin_users = admin_users

# Настройки cookie секрета
c.JupyterHub.cookie_secret = bytes.fromhex(
    os.getenv('JUPYTERHUB_COOKIE_SECRET', 'a' * 32)
)

# Настройки прокси
c.JupyterHub.proxy_auth_token = os.getenv('JUPYTERHUB_PROXY_AUTH_TOKEN', 'proxy-token')

# Хранение данных
c.JupyterHub.db_url = 'sqlite:///jupyterhub.sqlite'

# Разрешаем всем пользователям (для разработки)
c.Authenticator.allow_all = True

# Настройки для JupyterLab
c.Spawner.default_url = '/lab'

# Логирование
c.JupyterHub.log_level = 'DEBUG'
