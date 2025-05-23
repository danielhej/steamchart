# 🎮 Steam Chart Bot

> A simple Telegram bot for searching Steam games and comparing regional prices

<div align="center">

![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Steam](https://img.shields.io/badge/steam-%23000f1f.svg?style=for-the-badge&logo=steam&logoColor=white)

</div>

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 **Inline Search** | Type `@YourBotName game title` anywhere to search |
| 💰 **Price Compare** | Get prices across 4 different regions |
| 📱 **Rich Results** | Shows publisher, release date & thumbnails |
| ⚡ **Fast & Simple** | No registration needed, works instantly |

## 🚀 Quick Start

<details>
<summary><b>📋 Prerequisites</b></summary>

```bash
pip install python-telegram-bot requests
```

</details>

### 1️⃣ Get Bot Token
- Message [@BotFather](https://t.me/BotFather) 
- Use `/newbot` to create your bot
- Save the token (keep it secret!)

### 2️⃣ Enable Inline Mode  
- In BotFather: `/setinline`
- Set placeholder: `"Search Steam games..."`

### 3️⃣ Run the Bot
```bash
python bot.py
```

<div align="center">
🎉 <b>Your bot is now live!</b> 🎉
</div>

## 📱 How to Use

<table>
<tr>
<td width="50%">

**🔍 Search Games**
```
@YourBotName cyberpunk
@YourBotName witcher 3
@YourBotName elden ring
```

</td>
<td width="50%">

**💰 Compare Prices**

Just send any Steam link:
```
https://store.steampowered.com/app/1091500/
```

</td>
</tr>
</table>

### 🤖 Commands
- `/start` - Welcome message & instructions

## 🌍 Regional Coverage

<div align="center">

| Region | Flag | Currency |
|--------|------|----------|
| United States | 🇺🇸 | USD |
| Turkey | 🇹🇷 | TRY |  
| Argentina | 🇦🇷 | ARS |
| Russia | 🇷🇺 | RUB |

</div>

---

## ⚙️ Technical Details

<details>
<summary><b>🔧 APIs Used</b></summary>

- **Steam Store Search API** - Game discovery
- **Steam App Details API** - Game info & pricing  
- No API key required ✅

</details>

<details>
<summary><b>📊 Performance Notes</b></summary>

- Search limited to 10 results
- 2-second cache for inline queries
- Some prices may be unavailable in certain regions

</details>

---

## 🛡️ Security Warning

> ⚠️ **Never commit your bot token to version control!**
> 
> Use environment variables or `.env` files for sensitive data.

---

## 🚧 Contributing

Got ideas? Found bugs? PRs welcome!

**💡 Future Features:**
- Historical price tracking
- More regions  
- Wishlist notifications
- Game reviews integration

---

<div align="center">

**Made with ❤️ for Steam gamers**

⭐ Star this repo if it helped you save money on games!

</div>