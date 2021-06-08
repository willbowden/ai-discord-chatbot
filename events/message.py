import discord
import config
from env import Env

async def trigger(client, message):
    if message.author.bot: return
    if message.content.startswith(config.PREFIX):
        if str(message.author.id) not in config.AUTHORISED_IDS:
            errorEmbed = discord.Embed(title="**Insufficient Permission**", 
                description=f"You are not authorised to use this command.")
            return await message.channel.send(embed=errorEmbed)
        
        env = Env(client, message)

        for command in client.commands:
            if env.args[0] in command.names:
                return await command.execute(env)