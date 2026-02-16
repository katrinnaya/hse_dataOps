# ДЗ по теме 15: Создание Helm чарта
## Деплой несколько раз с разными настройками (команды выполняю внутри папки `nginx-helm`)
### Вариант 1. Стандартный деплой (с ресурсами и ingress)
```bash
helm install nginx-v1 ./nginx-helm
```
### Вариант 2. Деплой без лимитов ресурсов и без Ingress
Переопределение значения из `values.yaml` прямо в команде
```bash
helm install nginx-v2 ./nginx-helm --set resources.enabled=false --set ingress.enabled=false
```
### Вариант 3. Деплой с другой версией nginx
```bash
helm install nginx-v3 ./nginx-helm --set image.tag=1.25
```
#### Проверка
```bash
# Все релизы
helm list
# Созданные ресурсы (разные конфигурации)
kubectl get pods
kubectl get ingress
```
#### Удаление после проверки
```bash
helm uninstall nginx-v1
helm uninstall nginx-v2
helm uninstall nginx-v3
```


