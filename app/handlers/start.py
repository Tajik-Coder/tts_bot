"""
/start command handler.
"""

from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from app.keyboards.voice import voice_selection_keyboard
from app.states import TTSState

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message, state: FSMContext) -> None:
    """
    Entry point for the bot.
    """
    await state.clear()
    await message.answer(
        """Добро пожаловать! 👋
Я могу преобразовать текст в высококачественную речь.
Пожалуйста, выберите голос""",
        reply_markup=voice_selection_keyboard(),
    )
