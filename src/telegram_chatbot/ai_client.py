"""Claude AI client with per-user conversation history."""
import logging
from collections import defaultdict

import anthropic

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "you are a helpful assistant, be kind and motivate your companion, "
    "answer like a best friend"
)
MAX_HISTORY = 20  # keeps last 10 conversation turns per user


class AIClient:
    """Manages async Claude API calls with per-user conversation history."""

    def __init__(self) -> None:
        self._client = anthropic.AsyncAnthropic()
        self._histories: dict[int, list[dict]] = defaultdict(list)

    def clear_history(self, user_id: int) -> None:
        """Clear conversation history for a user.

        Args:
            user_id: Telegram user ID.
        """
        self._histories[user_id].clear()
        logger.info(f"Cleared history for user {user_id}")

    async def get_response(self, user_id: int, message: str) -> str:
        """Send a message to Claude and return the response.

        Args:
            user_id: Telegram user ID for per-user history tracking.
            message: The user's message text.

        Returns:
            Claude's text response.

        Raises:
            anthropic.APIError: If the API call fails.
        """
        history = self._histories[user_id]
        history.append({"role": "user", "content": message})

        # Trim history to stay within token limits
        if len(history) > MAX_HISTORY:
            history[:] = history[-MAX_HISTORY:]

        response = await self._client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=history,
        )

        reply = next(
            (block.text for block in response.content if block.type == "text"), ""
        )
        history.append({"role": "assistant", "content": reply})
        return reply
