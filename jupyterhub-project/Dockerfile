FROM python:3.14-slim

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    nodejs \
    npm \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем configurable-http-proxy через npm
RUN npm install -g configurable-http-proxy

# Создаем рабочую директорию
WORKDIR /srv/jupyterhub

# Копируем requirements.txt и устанавливаем Python зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем конфигурацию JupyterHub
COPY jupyterhub_config.py .

# Создаем директорию для данных
RUN mkdir -p /srv/jupyterhub/data

# Открываем порт для JupyterHub
EXPOSE 8000

# Запускаем JupyterHub
CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py"]
