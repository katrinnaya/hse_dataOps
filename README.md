# ДЗ по теме 14

## Описание
Обновление конфигурации nginx из ДЗ13:
- Добавлены `resources` (requests/limits)
- Увеличен `/dev/shm` до 128Mi через `emptyDir`
- Развернут Redis с собственными лимитами ресурсов

## Структура
- `nginx/` — обновлённый nginx с ресурсами и shared memory
- `redis/` — новый сервис Redis

## Применение
```bash
kubectl apply -f nginx/
kubectl apply -f redis/
```
Проверка
```bash
kubectl get pods
kubectl get service
```
