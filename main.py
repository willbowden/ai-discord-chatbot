from dotenv import load_dotenv
import importlib
import discord
import config
import os
from events import message as messageEvent

load_dotenv("A:\Will\Desktop\Coding\David 2\.env")
TOKEN = os.getenv("BOT_TOKEN")
client = discord.Client()

#Initialise commands
commands = []
commandNames = [f[:-3] for f in os.listdir("commands") if f.endswith(".py") and f != "__init__.py"]
for command in commandNames:
    commands.append(importlib.import_module("."+command, "commands"))
client.commands = commands


@client.event
async def on_ready():
    print(f"{client.user} logged in.")
    await client.change_presence(activity=discord.Activity(name="Online"))

@client.event
async def on_message(message):
    await messageEvent.trigger(client, message)

client.run(TOKEN)
