import telebot

TOKEN = "8298332620:AAFNcCzZqsixkz7GLAz_ncdsj4RjWW2BxpE"  # token shu yerda
bot = telebot.TeleBot(TOKEN)

# /start komandasi
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Salom! 🤖\nMen oddiy savol-javob botman.\nSavol yoz!")

# Oddiy savol-javob
@bot.message_handler(func=lambda message: True)
def reply(message):
    text = message.text.lower()

    if "salom" in text:
        bot.send_message(message.chat.id, "Salom! Qalaysan? 😊")

    elif "yaxshimisiz" in text:
        bot.send_message(message.chat.id, "Rahmat, yaxshiman! Senchi?")

    elif "isming nima" in text:
        bot.send_message(message.chat.id, "Men oddiy botman 🤖")

    elif "rahmat" in text:
        bot.send_message(message.chat.id, "Arzimaydi! 😊")

    else:
        bot.send_message(message.chat.id, "Kechirasiz, tushunmadim 😅")

# Botni ishga tushirish
bot.polling()