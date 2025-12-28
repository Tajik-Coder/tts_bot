"""
Text-to-Speech service using edge-tts.
Handles audio generation and cleanup.
"""

import uuid
import asyncio
import logging
from pathlib import Path
import edge_tts

logger = logging.getLogger(__name__)

VOICE_MAP = {
    "ru_male_1": "ru-RU-DmitryNeural",
    "ru_female_1": "ru-RU-SvetlanaNeural",
    "ru_male_2": "ru-RU-MaximNeural",
    "ru_female_2": "ru-RU-DariyaNeural",

    "en_male_us": "en-US-GuyNeural",
    "en_female_us": "en-US-JennyNeural",
    "en_male_uk": "en-GB-RyanNeural",
    "en_female_uk": "en-GB-SoniaNeural",

    "de_male": "de-DE-ConradNeural",
    "de_female": "de-DE-KatjaNeural",

    "tr_male": "tr-TR-AhmetNeural",
    "tr_female": "tr-TR-EmelNeural",

    "uz_male": "uz-UZ-SardorNeural",
    "uz_female": "uz-UZ-MadinaNeural",

    "it_male": "it-IT-DiegoNeural",
}


# Пути аудио
OUTPUT_DIR = Path("app/tmp")
OUTPUT_DIR.mkdir(exist_ok=True)


async def generate_speech(text: str, voice: str = "male") -> Path:
    """
    Generate speech audio from text using edge-tts.

    :param text: Text to convert
    :param voice: 'male' or 'female'
    :return: Path to generated audio file
    """
    voice_key = voice.lower()
    if voice_key not in VOICE_MAP:
        voice_key = "male"

    filename = f"{uuid.uuid4()}.mp3"
    output_path = OUTPUT_DIR / filename

    try:
        communicate = edge_tts.Communicate(
            text=text,
            voice=VOICE_MAP[voice_key],
        )
        await communicate.save(str(output_path))
        return output_path

    except Exception as exc:
        logger.exception("TTS generation failed")
        raise exc
