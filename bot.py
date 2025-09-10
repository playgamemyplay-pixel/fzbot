import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.voice_states = True  # مهم للروم الصوتي

bot = commands.Bot(command_prefix="!", intents=intents)

# ناخذ ID الروم الصوتي من متغير بيئة
VC_ID = int(os.getenv("1399470664129318944"))

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    channel = bot.get_channel(VC_ID)
    if channel and isinstance(channel, discord.VoiceChannel):
        if not channel.guild.voice_client:
            await channel.connect()
            print(f"🎧 Joined voice channel: {channel.name}")

bot.run(os.getenv("DISCORD_TOKEN"))