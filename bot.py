import os
import sys
import time
import discord
from utils.settings import Settings
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
import inspect

discord.Bot.sync_commands

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(intents=intents)
bot.settings = Settings()

def reloadcog(path: str):
    bot.reload_extension(path)

load_dotenv()
TOKEN = os.getenv("TOKEN")
if TOKEN == None:
    print("TOKEN not found in the .env file.")
    exit()

def load_cogs():
    print("Loading commands")
    try:
        #--To load views put them in on_ready.py !!!--
        bot.load_extension('commands.reviews')
        bot.load_extension("commands.tickets")
        bot.load_extension("commands.settingsCommands")
        bot.load_extension('commands.infraction')
        bot.load_extension("commands.say")
        bot.load_extension("commands.embed")
        
        #listeners
        print("Loading listeners")
        bot.load_extension('listeners.on_ready')
        bot.load_extension('listeners.on_join')
        print("Listeners Loaded")
        
    except Exception as e:
        print(f"could not load {e}")
        pass

load_cogs()

bot.run(TOKEN)