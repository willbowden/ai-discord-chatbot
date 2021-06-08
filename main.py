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
    activ = discord.CustomActivity(name="Online")
    await client.change_presence(activity=activ)

@client.event
async def on_message(message):
    await messageEvent.trigger(client, message)

@client.event
async def on_member_join(member):
    print(f"{member.name} joined.")
    if "twitter" in member.name.lower():
        channel = await client.get_channel(757687250635980933)
        await channel.send("Banning that stupid H0nde cunt for the millionth time!")
        await member.ban()

client.run(TOKEN)
