# Жги! Цех Backend API

**Проект:** Журнал современной керамики и стекла  
**Стек:** FastAPI, PostgreSQL, SQLAlchemy, Alembic  
**Версия:** 1.0.0

## 🚀 Быстрый старт

### Требования
- Docker & Docker Compose
- Git

### Установка

1. Клонируй репо:
git clone https://github.com/zhgi-tsekh/zhgi-tsekh-backend.git
cd zhgi-tsekh-backend

text

2. Создай .env файл:
cp .env.example .env

text

3. Запусти Docker:
docker compose up

text

4. Откройся браузер:
- **API Docs:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc
- **Health:** http://localhost:8000/health

## 📚 API Endpoints

### Masters
- `GET /api/v1/masters` - Получить всех мастеров
- `POST /api/v1/masters` - Создать нового мастера

### Events
- `GET /api/v1/events` - Получить все события
- `GET /api/v1/events/{id}` - Получить событие по ID

### System
- `GET /health` - Проверка здоровья
- `GET /api/v1/status` - Статус системы
- `GET /api/v1/version` - Версия API

## 🛠 Разработка

### Остановить сервисы
docker compose down

text

### Просмотр логов
docker compose logs -f api
docker compose logs -f postgres

text

### Пересобрать образы
docker compose up --build

text

## 📝 Лицензия

MIT License - 2025 Жги! Цех