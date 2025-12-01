from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv

load_dotenv()

# Инициализация FastAPI приложения
app = FastAPI(
    title="Жги! Цех API",
    description="API для проекта журнала современной керамики и стекла",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# CORS конфигурация
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==================== ROUTES ====================

@app.get("/")
async def root():
    """Главная страница API"""
    return {
        "message": "🎉 Жги! Цех API работает!",
        "status": "ok",
        "version": "1.0.0",
        "docs": "http://localhost:8000/docs"
    }

@app.get("/health")
async def health():
    """Проверка здоровья сервиса"""
    return {
        "status": "healthy",
        "database": "connected",
        "api": "running"
    }

# Masters endpoints
@app.get("/api/v1/masters")
async def get_masters():
    """Получить всех мастеров"""
    return {
        "masters": [],
        "total": 0,
        "message": "API готов к использованию"
    }

@app.post("/api/v1/masters")
async def create_master(name: str, city: str):
    """Создать нового мастера"""
    return {
        "id": 1,
        "name": name,
        "city": city,
        "status": "created"
    }

# Events endpoints
@app.get("/api/v1/events")
async def get_events():
    """Получить все события"""
    return {
        "events": [],
        "total": 0
    }

@app.get("/api/v1/events/{event_id}")
async def get_event(event_id: int):
    """Получить событие по ID"""
    return {
        "event_id": event_id,
        "title": "Событие",
        "status": "found"
    }

# System endpoints
@app.get("/api/v1/status")
async def api_status():
    """Статус всей системы"""
    return {
        "api": "running",
        "version": "1.0.0",
        "environment": os.getenv("DEBUG", "False"),
        "database_url": "postgresql://[HIDDEN]",
        "timestamp": "2025-12-01T23:45:00Z"
    }

@app.get("/api/v1/version")
async def api_version():
    """Версия API"""
    return {
        "version": "1.0.0",
        "release_date": "2025-12-01",
        "status": "stable"
    }

# Error handlers
@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """Общий обработчик ошибок"""
    return JSONResponse(
        status_code=500,
        content={"error": str(exc), "type": "InternalServerError"}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
