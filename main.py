import telebot
import instaloader
import os

# TOKEN (BotFather dan olasan)
TOKEN = "Bot_token"
bot = telebot.TeleBot(TOKEN)

# Instaloader obyekt
L = instaloader.Instaloader()

# /start komandasi
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Salom! 👋\n\nInstagram link yubor, men yuklab beraman 📥"
    )

# Instagram linkni ushlash
@bot.message_handler(func=lambda message: "instagram.com" in message.text)
def download_instagram(message):
    url = message.text.strip()

    try:
        bot.send_message(message.chat.id, "⏳ Yuklanmoqda...")

        # shortcode olish
        shortcode = url.split("/")[-2]

        post = instaloader.Post.from_shortcode(L.context, shortcode)

        # video bo‘lsa
        if post.is_video:
            video_url = post.video_url
            bot.send_video(message.chat.id, video_url)

        else:
            # rasm bo‘lsa
            for node in post.get_sidecar_nodes():
                bot.send_photo(message.chat.id, node.display_url)

            # agar oddiy bitta rasm bo‘lsa
            if not post.typename == "GraphSidecar":
                bot.send_photo(message.chat.id, post.url)

    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Xatolik: {e}")

# Botni ishga tushirish
bot.polling()
