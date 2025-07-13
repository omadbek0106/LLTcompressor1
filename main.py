import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = "8094418889:AAHSxYdCF78mFnOqddCQ2SA5bVkPEt27rPk"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def welcome(message: types.Message):
    await message.answer("🎬 Videoni yuboring va men uni qayta ishlab beraman")

@dp.message_handler(content_types=types.ContentType.VIDEO)
async def handle_video(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("📉 Hajmni kamaytirish", callback_data="compress"))
    keyboard.add(InlineKeyboardButton("🎥 Video sifati", callback_data="quality"))
    await message.reply("🎬 Video qabul qilindi!", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data)
async def process_callback(callback_query: types.CallbackQuery):
    data = callback_query.data
    if data == "compress":
        kb = InlineKeyboardMarkup(row_width=3)
        for i in range(10, 100, 10):
            kb.insert(InlineKeyboardButton(f"{i}%", callback_data=f"compress_{i}"))
        kb.add(InlineKeyboardButton("🔁 Qayta sozlash", callback_data="compress_reset"))
        await bot.send_message(callback_query.from_user.id, "📉 Siqish foizini tanlang:", reply_markup=kb)
    elif data == "quality":
        kb = InlineKeyboardMarkup()
        for res in ["144p", "240p", "360p", "480p", "720p", "1080p"]:
            kb.add(InlineKeyboardButton(res, callback_data=f"res_{res}"))
        await bot.send_message(callback_query.from_user.id, "🎥 Video sifatini tanlang:", reply_markup=kb)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
