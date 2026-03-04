# ДЗ по теме 18: Работа с БД в ML-проектах

## Файлы:
- `docker-compose.yaml` - конфигурация PostgreSQL
- `Makefile` - команды для управления миграциями
- `requirements.txt` - зависимости Python
- `.env.` - переменные окружения
- `migrations/` - файлы миграций базы данных

## Миграции:
1. `20240301_01_create_users_table.py` - создание таблицы users
2. `20240301_02_add_lastname_to_users.py` - добавление поля last_name

## Шаги выполнения:
1. Создание первой миграции (таблица users)
```bash
make db.migration.new name="users: create table"
```
2. Создание второй миграции (добавление поля lastname)
```bash
make db.migration.new name="add lastname to users"
```
3. Создание виртуального коружения и установка зависимостей
```bash
make dev.install
source venv/bin/activate 
```
4. Запуск PostgreSQL в Docker
```bash
make db.up
```
5. Миграции
```bash
make db.migrate
```
6. Проверка статуса
```bash
make db.status
```
7. Проверка результатов
```bash
# Подключиться к БД через psql
make db.psql

# Внутри psql выполнять:
\dt
SELECT * FROM users;
\d users
\q

$ make db.psql
Подключение к PostgreSQL...
docker exec -it postgres_db psql -U myuser -d mydatabase
psql (17.2)
Type "help" for help.

mydatabase=# \dt
              List of relations
 Schema |      Name      | Type  |  Owner   
--------+----------------+-------+----------
 public | users          | table | myuser
 public | yoyo_migration | table | myuser
 public | yoyo_lock      | table | myuser
(3 rows)

mydatabase=# \d users
                                            Table "public.users"
   Column   |            Type             | Collation | Nullable |              Default               
------------+-----------------------------+-----------+----------+------------------------------------
 id         | integer                     |           | not null | nextval('users_id_seq'::regclass)
 username   | character varying(100)      |           | not null | 
 email      | character varying(255)      |           | not null | 
 first_name | character varying(100)      |           |          | 
 last_name  | character varying(100)      |           |          | 
 created_at | timestamp with time zone    |           |          | CURRENT_TIMESTAMP
 updated_at | timestamp with time zone    |           |          | CURRENT_TIMESTAMP
Indexes:
    "users_pkey" PRIMARY KEY, btree (id)
    "users_email_key" UNIQUE CONSTRAINT, btree (email)
    "users_username_key" UNIQUE CONSTRAINT, btree (username)

mydatabase=# SELECT * FROM users;
 id | username | email | first_name | last_name | created_at | updated_at 
----+----------+-------+------------+-----------+------------+------------
(0 rows)

mydatabase=# \q
```
