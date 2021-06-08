import config
import discord

names = ["shutdown"]
async def execute(env):
    embed = discord.Embed(title="**GOODBYE**", description=f"{config.BOT_NAME} is shutting down.")
    await env.message.channel.send(embed=embed)
    exit()