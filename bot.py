from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ApplicationBuilder, InlineQueryHandler, MessageHandler, filters, CommandHandler
import requests
from uuid import uuid4
import re

def search_steam_games(query):
    url = f"https://store.steampowered.com/api/storesearch/?term={query}&cc=us&l=en"
    response = requests.get(url)
    data = response.json()
    return data.get("items", [])

async def inline_query(update, context):
    query = update.inline_query.query.strip()
    if not query:
        return

    games = search_steam_games(query)
    results = []

    for game in games[:10]:
        appid = game.get("id")
        game_info = get_app_details(appid)
        game_data = game_info.get(appid, {}).get("data", {})
        
        title = game.get("name")
        url = f"https://store.steampowered.com/app/{appid}"
        thumb = game.get("tiny_image", "")
        release_date = game_data.get("release_date", {}).get("date", "Unknown")
        publishers_list = game_data.get("publishers",{})
        publishers = " ".join(publishers_list)
        

        results.append(
            InlineQueryResultArticle(
                id=str(uuid4()),
                title=title,
                input_message_content=InputTextMessageContent(url, parse_mode="HTML"),
                description=f"Publishers: {publishers} | Date: {release_date}",
                thumbnail_url=thumb,
            )
        )

    await update.inline_query.answer(results, cache_time=2)

def get_app_details(appid):
    url = f"https://store.steampowered.com/api/appdetails?appids={appid}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()

def get_prices_by_region(appid):
    regions = {
        "us": "🇺🇸",
        "tr": "🇹🇷",
        "ar": "🇦🇷",
        "ru": "🇷🇺"
    }

    prices = []

    for region_code, flag in regions.items():
        url = f"https://store.steampowered.com/api/appdetails?appids={appid}&cc={region_code}&l=en"
        response = requests.get(url)
        if response.status_code != 200:
            continue
        data = response.json()
        try:
            price_info = data[str(appid)]["data"]["price_overview"]
            final = price_info["final_formatted"]
            prices.append(f"{flag} {final}")
        except Exception:
            prices.append(f"{flag} N/A")

    return "\n".join(prices)

async def message_handler(update, context):
    text = update.message.text.strip()
    pattern = r"https?://store\.steampowered\.com/app/(\d+)"
    match = re.search(pattern, text)

    if match:
        appid = match.group(1)
        prices_text = get_prices_by_region(appid)
        await update.message.reply_text(f"Prices for the game:\n{prices_text}")
    else:
        await update.message.reply_text("Please send a valid Steam game link.")

async def start(update, context):
    await update.message.reply_text(
        "🎮 Welcome to Steam Chart Bot!\n"
        "- Use inline mode (`@SteamChartBot <game name>`) to search games\n"
        "- Send a Steam game link to get prices in regions\n"
        "- More features coming soon!"
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token("8125395475:AAHXI592ieY66LEdQIyRYoo3Hd815UfeJYw").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(InlineQueryHandler(inline_query))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    app.run_polling()