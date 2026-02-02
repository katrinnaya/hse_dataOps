# ДЗ по теме 13: Введение в Kubernetes

## Описание
Развертывание веб-сервиса `nginx` в локальном кластере Kubernetes с использованием:
- `Deployment` — управление подами
- `Service` — внутренняя маршрутизация
- `Ingress` — внешний HTTP-доступ

Настроены пробы:
- `livenessProbe` — перезапускает под при сбое
- `readinessProbe` — отключает под от трафика, пока он не готов
- `startupProbe` — даёт дополнительное время на старт контейнера

## Требования
- Установка `kubectl`
```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
``` 
- Локальный кластер (`minikube`)
```bash
# Установка minikube 
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
# Запуск кластера
minikube start
```
- Установка Ingress Controller (`ingress-nginx`)
```bash
minikube addons enable ingress
```

## Развертывание
Применение манифестов
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml
```
Проверка статуса
```bash
kubectl get pods
kubectl get service
kubectl get ingress
```
Получение IP-адрес Ingress (в Minikube)
```bash
INGRESS_IP=$(minikube ip)
echo "Доступ по: http://$INGRESS_IP"
curl --header "Host: example.com" http://$INGRESS_IP/
```
