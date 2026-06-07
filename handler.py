from rubka import Bot
import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

bot = Bot(token="BEJGJH0AUMUZMSEGPDLMRMMEUXSNTBJUKUSBFZFKIOCXQMLQZBTUWLYFPKHGKSLJ")
ADMIN_USERNAME = "Ali_mosavii80"
STATS_FILE = "stats.json"

def load_stats():
    if os.path.exists(STATS_FILE):
        with open(STATS_FILE) as f:
            return json.load(f)
    return {"sent": 0, "deleted": 0, "clicks": 0}

def save_stats(stats):
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f)

@bot.on_message()
def handler(b, message):
    text = message.text or ""
    chat_id = message.chat_id
    username = getattr(message, "username", "")
    if text == "get_code":
        stats = load_stats()
        stats["clicks"] += 1
        save_stats(stats)
        bot.send_message(chat_id, "کد رفرال شما 👇\n`Cbie`\n\nروی کد نگه دارید تا کپی بشه ✅")
    if username == ADMIN_USERNAME:
        if text == "/start":
            bot.send_message(chat_id, "👋 سلام ادمین!\n\n/stats — آمار\n/status — وضعیت")
        elif text == "/stats":
            stats = load_stats()
            bot.send_message(chat_id, f"📊 آمار:\n\n📤 ارسالی: {stats['sent']}\n🗑️ حذفی: {stats['deleted']}\n👆 کلیک: {stats['clicks']}")
        elif text == "/status":
            bot.send_message(chat_id, "✅ ربات فعاله!")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")
    def log_message(self, format, *args):
        pass

port = int(os.environ.get("PORT", 10000))
server = HTTPServer(("0.0.0.0",

