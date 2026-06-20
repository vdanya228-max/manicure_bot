"""
Главный файл Telegram-бота для мастера маникюра.
"""
import sys
from pathlib import Path

# === Жёсткий фикс пути для Render.com и Railway ===
BASE_DIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, "/opt/render/project/src")   # Для Render
sys.path.insert(0, "/app")                      # Для Railway

import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiohttp import web

from config import BOT_TOKEN, ADMIN_ID
from database import init_db
from scheduler import init_scheduler, restore_reminders, shutdown_scheduler

# Импорт роутеров
from handlers.start import router as start_router
from handlers.booking import router as booking_router
from handlers.admin import router as admin_router
from handlers.common import router as common_router

# ... остальной код остаётся без изменений ...
