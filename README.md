# Team Finder

Платформа для поиска команды в проекты (аналог доски объявлений).
Финальный проект Яндекс Практикум.

## Функциональность
- Регистрация и аутентификация пользователей.
- Создание проектов с указанием требуемых навыков (тегов).
- Фильтрация проектов по навыкам (Вариант 3).
- Возможность вступать в проекты и покидать их.
- Публичные профили пользователей.

## Технологии
- Python 3.10+
- Django 4+
- PostgreSQL
- Docker & Docker Compose
- Bootstrap 5

## Запуск проекта (Локально)

1. Клонировать репозиторий:
   ```bash
   git clone <ссылка на репозиторий>
   cd team_finder_repo
   ```

2. Создать и активировать виртуальное окружение:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Linux/macOS
    # venv\Scripts\activate   # Для Windows
    ```

3. Установить зависимости:

    ```bash
    pip install -r backend/requirements.txt
    ```

4. Выполнить миграции и запустить:

    ```bash
    cd backend
    python manage.py migrate
    python manage.py runserver
    ```
