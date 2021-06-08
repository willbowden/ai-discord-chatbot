import discord
from ..util import wbjson
import config
import time
from ..training import gatherDataset

names = ["backtrain"]
async def execute(env):
    messsage = env.message
    args = env.args

    if not args[1] or not args [2] or not args [3]:
        errorEmbed = discord.Embed(title="**ERROR**", 
                description=f"Please specify args [channelID, beforeID, number]")
        return await message.channel.send(embed=errorEmbed)

    try:
        args[3] = int(args[3])
    except:
        errorEmbed = discord.Embed(title="**ERROR**", 
                description=f"'Number' argument should be an integer.")
        return await message.channel.send(embed=errorEmbed)
    
    if args[3] > 250:
        embed = discord.Embed(title="**WARNING**", 
                description=f"You've requested a lot of messages. Be prepared to wait.")
        return await message.channel.send(embed=embed)

    dataset = gatherDataset(args[1], args[2], args[3])
    wbjson.WriteRaw(str(time.time()) + ".json", dataset)