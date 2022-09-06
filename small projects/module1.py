import discord
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

from discord.ext import commands
client = commands.Bot(command_prefix='#', intents=intents)

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server...')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')

client.run('OTAyOTYwNTIyMjA1NDcwNzUw.YXmBhA.mACv0p5XP1aP3-A715wMSb5sejc')
