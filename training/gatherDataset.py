import os
from util import wbjson
import config

async def gatherDataset(env, channelID,  beforeID, number):
    channel = env.client.get_channel(channelID)
    messages = await channel.history(limit=number, before=beforeID)
    filteredMessages = {}

    for i in range(len(messages)):
        if messages[i].author.id == config.TRAINING_USER_ID:
            try:
                prevMessages = [messages[i-1].content, messages[i-2].content, messages[i-3].content]
            except:
                print("Reached start of message backlog. Cannot find previous messages")
                prevMessages = []
    
            filteredMessages.append({"response": messages[i].content, "previous": prevMessages})
    
    print(f"Done. Messages from designated user found: {len(filteredMessages)}")
    return filteredMessages



