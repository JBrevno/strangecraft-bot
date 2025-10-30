import os
import discord

# Токен читается из переменной окружения BOT_TOKEN
TOKEN = "MTExNzY5NjQ1MTI2NzUzMDg2NA.GXATnW.wuv7SP7ISucz1o8tro-P6U1wmya9VMOlBz_1YA"
if not TOKEN:
    raise SystemExit("❌ BOT_TOKEN не найден. Укажи его в переменной окружения или в /etc/default/strangecraft-bot")

# Минимальные разрешения (intents)
intents = discord.Intents.default()

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Бот вошёл в сеть как {bot.user}")
    await bot.change_presence(activity=discord.Game("StrangeCraft"))

bot.run(TOKEN)
