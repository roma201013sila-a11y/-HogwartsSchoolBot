import os
import telebot
from telebot import types

# Ботты дайын токен арқылы қосамыз
TOKEN = '8863616395:AAEs67fp3aG_g93W15bMZbuvlMBSfc69_-Y'
bot = telebot.TeleBot(TOKEN)

# Басты меню /start командасы
@bot.message_handler(commands=['start'])
def send_welcome(markup_chat):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('📚 Үй тапсырмалары')
    item2 = types.KeyboardButton('🧙‍♂️ Мұғалімдер')
    item3 = types.KeyboardButton('🏰 Мектеп туралы')
    markup.add(item1, item2, item3)
    
    bot.reply_to(markup_chat, "Қош келдіңіз, Хогвартс мектебінің оқушысы! ✨\nТөмендегі түймелер арқылы қажетті бөлімді таңдаңыз:", reply_markup=markup)

# Мәзір түймелерінің жұмысы
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

# Ботты үздіксіз іске қосып тұру
if __name__ == '__main__':
    print("Бот жұмыс істей бастады...")
    bot.infinity_polling()
