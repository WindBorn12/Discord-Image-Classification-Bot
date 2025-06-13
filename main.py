import discord
from discord.ext import commands
from model import Type_selector
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for image in ctx.message.attachments:
            await image.save(f"./Images/{image.filename}")
            await ctx.send(f"your photo has been saved --->{image.filename}")
            result = Type_selector(f"./Images/{image.filename}")
            await ctx.send(result)
    else:
        await ctx.send("Please add a image")

# TOKEN doğrudan yazılmıyor, ortam değişkeninden okunuyor
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
if TOKEN is None:
    raise ValueError("DISCORD_BOT_TOKEN environment variable not set!")
bot.run(TOKEN)