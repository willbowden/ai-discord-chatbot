import discord
from util import wbjson

names = ["stats", "info"]
async def execute(env):
    stats = wbjson.ReadFile("stats.json")
    userString = "No users have contributed."

    if len(stats.users) > 0:
        userString = ""
        for user in stats.users:
            userString += f"\n{user.id}: {user.number}"

    errorEmbed = discord.Embed(title="**STATISTICS**",
            description=f"""**Number of training items added:**
            \nGreetings: {str(stats.greeting)}
            \nGoodbyes: {str(stats.goodbye)}
            \nInsults: {str(stats.insult)}
            \nCompliments: {str(stats.compliment)}
            {userString}""")
    await env.message.channel.send(embed=errorEmbed)