from os import environ
import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup


API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
API_KEY = ('278d43c97ad2c336f5a41369e0bb7f803e3b4675')
#don't edit API_KEY because you can't get API_KEY at this time! ✖️✖️

bot = Client('gplink bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)


@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**Hi {message.chat.first_name}!**\n\n"
        "I'm GPlink bot. I will create a link that can verify user and then authorise him to use your given URL! \n Just send me link and get short link",
                         reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             " 🏷️  Channel ", url="https://t.me/RobotTech_official")
                       ],[
                          InlineKeyboardButton(
                             "🌐 Source Code ", url="https://gplinks.co/DVScQs8")
                       ]]
                   ))


@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    try:
        short_link = await get_shortlink(link)
        await message.reply(f'Below Is your Public link that can be shared! If that button doesnt work then 🏷️ Here is your\n  {short_link}', quote=True,
                             reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "🚀 Your Link ", url="{short_link}")
                       ]]
                   ))
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)


async def get_shortlink(link):
    url = 'https://gplinks.in/api'
    params = {'api': API_KEY, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]


bot.run()
