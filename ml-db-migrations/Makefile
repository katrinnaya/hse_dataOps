# Makefile для управления миграциями БД

# Загрузка переменных окружения
include .env
export

# Цвета для вывода
GREEN = \033[0;32m
RED = \033[0;31m
NC = \033[0m # No Color

.PHONY: help dev.install db.migration.new db.migrate db.rollback db.up db.down db.status

help: ## Показать эту справку
	@printf "${GREEN}Доступные команды:${NC}\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "${GREEN}%-20s${NC} %s\n", $$1, $$2}'

dev.install: ## Установка зависимостей проекта
	@printf "${GREEN}Установка зависимостей...${NC}\n"
	python -m venv venv
	. venv/bin/activate && pip install --upgrade pip
	. venv/bin/activate && pip install -r requirements.txt
	@printf "${GREEN}Зависимости установлены. Активируйте виртуальное окружение: source venv/bin/activate${NC}\n"

db.up: ## Запуск PostgreSQL в Docker
	@printf "${GREEN}Запуск PostgreSQL...${NC}\n"
	docker compose up -d db
	@printf "${GREEN}Ожидание готовности PostgreSQL...${NC}\n"
	@until docker exec ${POSTGRES_CONTAINER_NAME} pg_isready -U ${POSTGRES_USER} > /dev/null 2>&1; do \
		printf "."; \
		sleep 1; \
	done
	@printf "\n${GREEN}PostgreSQL готов к работе${NC}\n"

db.down: ## Остановка PostgreSQL
	@printf "${GREEN}Остановка PostgreSQL...${NC}\n"
	docker compose down

db.migration.new: ## Создание новой миграции (использовать: make db.migration.new name="название миграции")
	@if [ -z "$(name)" ]; then \
		printf "${RED}Ошибка: укажите название миграции (name=\"название\")${NC}\n"; \
		exit 1; \
	fi
	@printf "${GREEN}Создание миграции: $(name)...${NC}\n"
	@. venv/bin/activate && \
	cd migrations && \
	yoyo new ./ -m "$(name)"
	@printf "${GREEN}Миграция создана. Отредактируйте файл в папке migrations/${NC}\n"

db.migrate: ## Применение всех миграций
	@printf "${GREEN}Применение миграций...${NC}\n"
	@. venv/bin/activate && \
	yoyo apply --database $(DB_URL) ./migrations/
	@printf "${GREEN}Миграции применены${NC}\n"

db.rollback: ## Откат последней миграции
	@printf "${GREEN}Откат последней миграции...${NC}\n"
	@. venv/bin/activate && \
	yoyo rollback --database $(DB_URL) ./migrations/ --one
	@printf "${GREEN}Миграция откачена${NC}\n"

db.status: ## Показать статус миграций
	@printf "${GREEN}Статус миграций:${NC}\n"
	@. venv/bin/activate && \
	yoyo list --database $(DB_URL) ./migrations/

db.psql: ## Подключиться к БД через psql
	@printf "${GREEN}Подключение к PostgreSQL...${NC}\n"
	@docker exec -it ${POSTGRES_CONTAINER_NAME} psql -U ${POSTGRES_USER} -d ${POSTGRES_DB}

clean: ## Очистка виртуального окружения
	@printf "${GREEN}Очистка...${NC}\n"
	rm -rf venv
	rm -rf __pycache__
	rm -rf .pytest_cache
	@printf "${GREEN}Очистка завершена${NC}\n"
