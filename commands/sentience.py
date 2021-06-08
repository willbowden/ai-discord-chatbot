import discord
import os
from util import wbjson
import config

names = ["sentience"]
async def execute(env):
    message = env.message
    args = env.args
    if not args[1]:
        errorEmbed = discord.Embed(title="**ERROR**", 
                description=f"Please specify [on / off]")
        return await message.channel.send(embed=errorEmbed)
    
    if args[1] not in ["on", "off"]:
        errorEmbed = discord.Embed(title="**Error**", 
                description=f"Invalid option. Please specify [on / off]")
        return await message.channel.send(embed=errorEmbed)

    meta = wbjson.ReadFile("meta.json")
    if args[1] == "on":
        meta.active = True
        desc = config.BOT_NAME + " is now online."
        await env.client.change_presence(activity=discord.Activity(name="Auto-Reply On"))
    else:
        meta.active = False
        desc = config.BOT_NAME + " is now offline."
        await env.client.change_presence(activity=discord.Activity(name="Auto-Reply Off"))

    wbjson.WriteFile("meta.json", meta)
    successEmbed = discord.Embed(title="**SUCCESS**", description=desc)
    await message.channel.send(embed=successEmbed)
