"""
Application configuration module.
Loads environment variables securely using python-dotenv.
"""

from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Config:
    """Global application configuration."""
    bot_token: str


def load_config() -> Config:
    """Load and validate environment configuration."""
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN is not set in environment variables")

    return Config(bot_token=token)
