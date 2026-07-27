import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from google import genai

# Токендерді осы жерге жазасың
TELEGRAM_BOT_TOKEN = "ТЕЛЕГРАМ_БОТ_ТОКЕНІҢДІ_ЖАЗ"
GEMINI_API_KEY = "GEMINI_API_KEY_КІЛТІҢДІ_ЖАЗ"

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()
client = genai.Client(api_key=GEMINI_API_KEY)

# --- /start КОМАНДАСЫ ЖӘНЕ ХОГВАРСТ СТИЛІНДЕГІ СӘЛЕМДЕСУ ---
@dp.message(Command("start"))
async def send_welcome(message: Message):
    welcome_text = (
        "✨ **Добро пожаловать в Hogwarts School!** ✨\n\n"
        "🏰 Сәлем, сиқыршы! Мен — HogwartsSchoolBot 🪄\n\n"
        "📚 Мен саған кез келген істе көмектесе аламын:\n"
        "🤖 AI-мен еркін сөйлесу\n"
        "📖 Кез келген сұраққа жауап беру\n"
        "🖼️ Фото жасау және өңдеу\n"
        "🎨 Логотип, баннер, постер дайындау\n"
        "📄 Word, PDF, PowerPoint жасау\n"
        "💻 HTML • CSS • JavaScript • Python код жазу\n"
        "🌐 Веб-сайт құру\n"
        "📊 Кесте, жоспар, презентация жасау\n"
        "🌍 Аударма жасау\n"
        "🧙 Hogwarts Academy жүйесімен жұмыс істеу\n\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "🪄 **Hogwarts AI дайын!**\n"
        "💬 Маған кез келген сұрақты жаза аласың.\n\n"
        "Мысалы:\n"
        "• Фото жасап бер\n"
        "• Сайт жасап бер\n"
        "• PowerPoint жаса\n"
        "• Код жаз\n"
        "• Үй тапсырмасын орында\n"
        "• Суретті өңде\n"
        "• Логотип жаса\n"
        "• Мәтінді аудар\n\n"
        "✨ Мен әрқашан көмектесуге дайынмын."
    )
    await message.answer(welcome_text, parse_mode="Markdown")

# --- БАТЫРМАСЫЗ, ТЕК ӘҢГІМЕЛЕСУ ЖӘНЕ СҰРАҚҚА ЖАУАП БЕРУ ---
@dp.message()
async def chat_with_ai(message: Message):
    text = message.text
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=text,
        )
        await message.answer(response.text)
    except Exception as e:
        await message.answer("⚡ Сиқырлы байланыста қателік кетті, кейінірек көріңізші!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
