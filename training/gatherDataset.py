import os
from util import wbjson
import time
import config

async def gatherDataset(env, channelID,  beforeID, number):
    channel = env.client.get_channel(int(channelID))
    beforeMsg = await channel.fetch_message(int(beforeID))
    messages = await channel.history(limit=int(number), before=beforeMsg).flatten()
    print(messages)
    filteredMessages = []

    for i in range(len(messages)):
        if messages[i].author.id == int(config.TRAINING_USER_ID) or messages[i].author.name == config.TRAINING_USER_NAME:
            try:
                prevMessages = [messages[i+1].content, messages[i+2].content, messages[i+3].content]
            except:
                print("Reached start of message backlog. Cannot find previous messages")
                prevMessages = []
    
            filteredMessages.append({"response": messages[i].content, "previous": prevMessages})
    
    print(f"Done. Messages from designated user found: {len(filteredMessages)}")
    return filteredMessages
    #print(filteredMessages)
    #wbjson.WriteRaw(str(time.time()) + ".json", filteredMessages)



