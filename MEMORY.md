# Telegram Chatbot — Project Memory

## Purpose
A simple async Telegram chatbot that uses Claude claude-opus-4-6 as the AI backend. Each user gets their own conversation history with a "best friend" persona.

## Status
✅ Complete and ready to run.

## Stack
- **aiogram 3.x** — async Telegram bot framework with Router/Dispatcher pattern
- **anthropic 0.86** — Claude API SDK (AsyncAnthropic for non-blocking calls)
- **python-dotenv** — loads `.env` file for secrets
- **UV** — package and venv management

## Architecture
```
src/telegram_chatbot/
    main.py       — Bot + Dispatcher setup, entry point
    handlers.py   — /start, /clear, and message handlers (single Router)
    ai_client.py  — AIClient: async Claude calls + per-user history dict
```

## Key Design Decisions
- `AIClient` uses `AsyncAnthropic` — no blocking calls in the async event loop
- Per-user history stored in a `defaultdict[int, list]` (resets on restart)
- `ChatActionSender.typing()` context manager keeps the typing indicator alive for the full API call duration
- History capped at `MAX_HISTORY = 20` messages (~10 turns) to control token usage
- HTML parse mode enabled by default via `DefaultBotProperties`

## System Prompt
```
you are a helpful assistant, be kind and motivate your companion, answer like a best friend
```

## How to Run
```bash
cd C:/Users/User/.claude/projects/telegram_chatbot
cp .env.example .env        # then add your TELEGRAM_BOT_TOKEN
uv run python -m telegram_chatbot.main
```

## Required Env Vars
- `TELEGRAM_BOT_TOKEN` — from @BotFather on Telegram
- `ANTHROPIC_API_KEY` — already exported in ~/.bashrc

## Known Gotchas
- History resets on bot restart (in-memory only, no persistence)
- Python 3.14 is installed — aiogram 3.x is fully compatible
