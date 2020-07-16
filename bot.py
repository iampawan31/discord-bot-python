import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()


@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(activity=discord.Game("Making a bot"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Hello":
        await message.channel.send('World')
    if message.content == 'Hey Bot':
        await message.channel.send('Yes?')
    if message.content == 'How are you?':
        await message.channel.send('I am fine. How are you?')

client.run(TOKEN)
