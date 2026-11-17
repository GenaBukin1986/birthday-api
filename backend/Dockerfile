FROM python:3.11-slim

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry

WORKDIR /app

# Копируем файлы зависимостей (они теперь рядом!)
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости без виртуального окружения
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --only main

# Копируем код приложения
COPY ./app ./app

# Запускаем сервер
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]