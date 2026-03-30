"""Telegram message and command handlers."""
import logging

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.utils.chat_action import ChatActionSender

from .ai_client import AIClient

logger = logging.getLogger(__name__)
router = Router()
_ai = AIClient()


@router.message(CommandStart())
async def handle_start(message: Message) -> None:
    """Greet the user and explain available commands."""
    await message.answer(
        "Hey! 👋 I'm your friendly AI companion powered by Claude!\n\n"
        "I'm here to chat, help, and cheer you on — just talk to me like a friend.\n\n"
        "📌 <b>/clear</b> — reset our conversation and start fresh"
    )


@router.message(Command("clear"))
async def handle_clear(message: Message) -> None:
    """Reset conversation history for the user."""
    if message.from_user:
        _ai.clear_history(message.from_user.id)
    await message.answer("Done! 🌟 Fresh start — what's on your mind?")


@router.message()
async def handle_message(message: Message) -> None:
    """Forward any text message to Claude and reply with the response."""
    if not message.text or not message.from_user:
        return

    # ChatActionSender keeps "typing..." alive for the full duration of the API call
    async with ChatActionSender.typing(bot=message.bot, chat_id=message.chat.id):
        try:
            reply = await _ai.get_response(message.from_user.id, message.text)
        except Exception:
            logger.exception("Error calling Claude API")
            await message.answer("Oops, something went wrong on my end. Try again in a sec! 😅")
            return

    await message.answer(reply)
