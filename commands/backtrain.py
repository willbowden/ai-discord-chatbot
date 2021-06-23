import discord
from util import wbjson
import config
import asyncio
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
    for i in range(len(dataset)):

        embed = discord.Embed(title=f"**{dataset[i]['response']}**",
            description="Is this a response to a [1. Greeting] [2. Goodbye] [3. Insult] or [4. Compliment]")
        await env.message.channel.send(embed=embed)

        def check(m):
                return m.content, m.author == env.message.author

        try:
            message, user = await env.client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await env.channel.send('**Error: Timeout**')
        else:
            if message == "1":
                return
