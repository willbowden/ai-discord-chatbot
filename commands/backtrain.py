import discord
from util import wbjson
import config
import time
from training import gatherDataset

names = ["backtrain"]
async def execute(env):
    args = env.args

    if len(args) < 4:
        errorEmbed = discord.Embed(title="**ERROR**", 
                description=f"Please specify args [channelID, beforeID, number]")
        return await env.message.channel.send(embed=errorEmbed)

    try:
        args[3] = int(args[3])
    except:
        errorEmbed = discord.Embed(title="**ERROR**", 
                description=f"'Number' argument should be an integer.")
        return await env.message.channel.send(embed=errorEmbed)
    
    if args[3] > 250:
        embed = discord.Embed(title="**WARNING**", 
                description=f"You've requested a lot of messages. Be prepared to wait.")
        return await env.message.channel.send(embed=embed)

    dataset = await gatherDataset.gatherDataset(env, args[1], args[2], args[3])
    del dataset
    embed = discord.Embed(title="**COMPLETE**", 
        description=f"The dataset has been processed and saved to the directory.")
    return await env.message.channel.send(embed=embed)