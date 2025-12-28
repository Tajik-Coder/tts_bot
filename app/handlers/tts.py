import logging
from aiogram import Router
from aiogram.types import CallbackQuery, Message, FSInputFile
from aiogram.fsm.context import FSMContext
from app.states import TTSState
from app.services.tts_service import generate_speech, VOICE_MAP

router = Router()
logger = logging.getLogger(__name__)


@router.callback_query()
async def voice_selected(callback: CallbackQuery, state: FSMContext) -> None:
    voice_key = callback.data

    if voice_key not in VOICE_MAP:
        await callback.answer("Это не голос ❌", show_alert=True)
        return

    await state.update_data(voice=voice_key)
    await state.set_state(TTSState.waiting_for_text)

    await callback.message.answer(
        "Голос выбран ✅\n\nTеперь введите текст."
    )
    await callback.answer()


@router.message(TTSState.waiting_for_text)
async def text_to_speech(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    voice = data.get("voice")

    if not voice:
        await message.answer("Сначала выберите голос❗")
        return

    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action="upload_audio",
    )

    audio_path = None

    try:
        audio_path = await generate_speech(message.text, voice)
        await message.answer_audio(
            audio=FSInputFile(audio_path),
            caption="🎧 Готово",
        )
    except Exception:
        logger.exception("TTS error")
        await message.answer("Произошла ошибка ❌")
    finally:
        if audio_path and audio_path.exists():
            audio_path.unlink()
