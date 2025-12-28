"""
Application entry point.
Initializes bot, dispatcher, routers, and starts polling.
"""

import asyncio
from aiogram import Bot, Dispatcher
from app.config import load_config
from app.logger import setup_logging
from app.handlers import start, tts


async def main() -> None:
    """Main application runner."""
    setup_logging()
    config = load_config()

    bot = Bot(token=config.bot_token)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(tts.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Bot started...")
    asyncio.run(main())
