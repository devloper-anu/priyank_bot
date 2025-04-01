import os
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Logging setup
logging.basicConfig(level=logging.INFO)

# Environment Variables (Render pe set karna)
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable not set!")

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Start command
@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("🎵 Welcome to the Telegram Music Bot! Send a song name to search.")

# Help command
@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer("🎵 Use /start to begin and send a song name to search for music!")

# Handle text messages
@dp.message()
async def handle_music_request(message: types.Message):
    await message.answer(f"🔍 Searching for: {message.text} (Feature Coming Soon!)")

# Main function
async def main():
    logging.info("Starting bot...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())