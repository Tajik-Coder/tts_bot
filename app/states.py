"""
FSM states for user interaction.
"""

from aiogram.fsm.state import StatesGroup, State


class TTSState(StatesGroup):
    """States related to text-to-speech workflow."""
    waiting_for_text = State()
