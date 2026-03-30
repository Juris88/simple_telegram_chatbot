# Launch Instructions

## New Machine Setup

### 1. Open terminal and Install UV (package manager)
MAC OS
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
On Windows (PowerShell):
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Clone the repo and install dependencies
```bash
git clone https://github.com/Juris88/simple_telegram_chatbot
cd simple_telegram_chatbot
uv sync          # creates .venv and installs all packages from uv.lock
```

### 3. Set up environment variables
```bash
cp .env.example .env
# Open .env and fill in:
#   TELEGRAM_BOT_TOKEN=your_token_from_BotFather
#   ANTHROPIC_API_KEY=your_anthropic_api_key
```

> **Get your tokens:**
> - Telegram token → [@BotFather](https://t.me/BotFather) → `/newbot`
> - Anthropic key → [console.anthropic.com](https://console.anthropic.com)

### 4. Run the bot
```bash
uv run python -m telegram_chatbot.main
```

---

## Daily Start (existing machine)
```bash
cd telegram_chatbot
uv run python -m telegram_chatbot.main
```

## Stop the Bot
Press `Ctrl+C` in the terminal.

---

## Available Commands (in Telegram)
| Command  | Description                          |
|----------|--------------------------------------|
| `/start` | Greeting and intro message           |
| `/clear` | Reset your conversation history      |
| Any text | Chat with the AI (best-friend style) |

## Expected Output
```
2025-03-29  INFO  telegram_chatbot.main — Bot is starting — press Ctrl+C to stop
```

## Configuration (`.env` file)
| Variable            | Required | Description                        |
|---------------------|----------|------------------------------------|
| `TELEGRAM_BOT_TOKEN` | ✅       | Bot token from @BotFather          |
| `ANTHROPIC_API_KEY`  | ✅       | Key from console.anthropic.com     |
