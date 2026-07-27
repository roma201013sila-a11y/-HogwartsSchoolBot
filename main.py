import os
import telebot
from telebot import types

TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('📚 Үй тапсырмалары')
    item2 = types.KeyboardButton('🧙‍♂️ Мұғалімдер')
    item3 = types.KeyboardButton('🏰 Мектеп туралы')
    markup.add(item1, item2, item3)
    
    bot.reply_to(message, "Қош келдіңіз, Хогвартс мектебінің оқушысы! ✨\nТөмендегі түймелер арқылы қажетті бөлімді таңдаңыз:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text == '📚 Үй тапсырмалары':
        bot.reply_to(message, "Бүгінгі үй тапсырмалары:\n\n1. Шағын зельвар қайнату (Практика)\n2. Маглану танудан конспект жазу.")
    elif message.text == '🧙‍♂️ Мұғалімдер':
        bot.reply_to(message, "Біздің мектептің оқытушылары:\n• Рамазан — Директор, Маглану тану, Аппарация және практикалық сабақтар.")
    elif message.text == '🏰 Мектеп туралы':
        bot.reply_to(message, "Hogwarts School KZ — сиқыр мен білім ордасы! ⚡")
    else:
        bot.reply_to(message, "Түсініксіз команда. Мәзірден батырманы таңдаңыз немесе /start басыңыз.")

if __name__ == '__main__':
    bot.infinity_polling()
