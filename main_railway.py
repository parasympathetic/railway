#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import asyncio
import logging
from datetime import datetime, timedelta
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes
)

# Завантажуємо змінні з .env файлу
load_dotenv()

# Налаштування логування
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# 🔵 Статті
articles = [
    "Стаття 1: Вступ до медитації — як працює розум.",
    "Стаття 2: Дихання як інструмент заспокоєння.",
    "Стаття 3: Як зменшити стрес через усвідомленість.",
    "Стаття 4: Парасимпатична нервова система: що це і як її активувати.",
    "Стаття 5: Роль фізичних вправ у подоланні тривожності."
]

user_progress = {}

# 🔵 /start команда
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_progress[chat_id] = {
        'index': 1,
        'last_sent': datetime.now()
    }

    logger.info(f"Користувач {chat_id} запустив бота")
    
    await update.message.reply_text("Привіт! Я надсилатиму тобі нову статтю кожні 5 хвилин 📰")
    await context.bot.send_message(chat_id=chat_id, text=articles[0])

    # Запускаємо повторювану задачу
    context.job_queue.run_repeating(
        send_article_if_due,
        interval=timedelta(minutes=5),
        first=timedelta(minutes=5),
        chat_id=chat_id
    )

# 🔵 Перевірка та надсилання статей
async def send_article_if_due(context: ContextTypes.DEFAULT_TYPE):
    chat_id = context.job.chat_id
    progress = user_progress.get(chat_id)

    if not progress:
        return

    now = datetime.now()
    idx = progress['index']
    last_sent = progress['last_sent']

    if idx < len(articles) and (now - last_sent) >= timedelta(minutes=5):
        await context.bot.send_message(chat_id=chat_id, text=articles[idx])
        user_progress[chat_id] = {
            'index': idx + 1,
            'last_sent': now
        }
        logger.info(f"Надіслано статтю {idx + 1} користувачу {chat_id}")
    elif idx >= len(articles):
        await context.bot.send_message(
            chat_id=chat_id,
            text="🟢 Всі статті надіслано. Дякую, що читав(ла)!"
        )
        logger.info(f"Всі статті надіслано користувачу {chat_id}")

# 🔵 Обробка помилок
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error(f"Exception while handling an update: {context.error}")

# 🔹 Запуск бота
async def main():
    # Отримуємо токен з змінних середовища
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not bot_token:
        logger.error("TELEGRAM_BOT_TOKEN не знайдено в змінних середовища!")
        return

    logger.info("Запуск Telegram бота на Railway...")

    # Створюємо додаток
    app = ApplicationBuilder().token(bot_token).build()

    # Додаємо обробники
    app.add_handler(CommandHandler("start", start))
    app.add_error_handler(error_handler)

    logger.info("Бот запущено на Railway - 24/7 режим")
    
    # Запускаємо бота
    await app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот зупинено користувачем")
    except Exception as e:
        logger.error(f"Критична помилка: {e}")
        raise
