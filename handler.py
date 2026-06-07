from rubka import Bot

bot = Bot(token="BEJGJH0AUMUZMSEGPDLMRMMEUXSNTBJUKUSBFZFKIOCXQMLQZBTUWLYFPKHGKSLJ")

@bot.on_message()
def handler(b, message):
    print(f"پیام دریافت شد: {message.text}")
    bot.send_message(message.chat_id, "سلام!")

print("شروع...")
bot.run()
