# Pyrogram Userbot Example

A clean, async-ready userbot template built with [**Kurigram** (Pyrogram fork)] and [**Dispyro**] for scalable dependency injection.

> ⚙️ Kurigram supports the latest MTProto API features. Dispyro adds flexible DI and middleware layers for better architecture.


---

## 🚀 Key Features

- ⚡ **uvloop** — faster event loop (Linux-only)
- 📦 **Poetry** — modern dependency and virtualenv manager
- 🐬 **MySQL** via **asyncmy** using repository pattern
- 🧠 **DBPool middleware** — injects **MySQL + Redis** into context
- 📝 **Logging** — bot startup, messages, errors
- 🔁 **pm2** — for process management & production deployment

---

## ⚙️ Installation

```bash
git clone https://github.com/SkrudjReal/single-pyrouserbot-example.git
cd single-pyrouserbot-example
poetry install --no-root
cp settings.env.example settings.env  # Create and edit environment config
```

## Start

## Development

```bash
poetry run python3 app.py
```

## Production via pm2

# With ecosystem file
```bash
pm2 start ecosystem.config.js
pm2 save && pm2 startup
```

# or manually
```bash
pm2 start "poetry run python3 app.py" --name "pyrogram-example"
pm2 save && pm2 startup
```

You are amazing.