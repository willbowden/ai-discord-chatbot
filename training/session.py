import os
import discord
import time
from util import wbjson
from types import SimpleNamespace
import random
import asyncio

sessions = {}
lastcommand = 0
model = None

def addPattern(id, _type):
    sessions[id] = {"mode": "pattern",
    "type": _type,
    "messages": [],
    "lastmessage": time.time()}

def addResponse(id, _type, question):
    sessions[id] = {"mode": "response",
    "type": _type,
    "messages": [],
    "question": question,
    "lastmessage": time.time()}

def remove(id):
    sessions.remove(id)

def receive(message):
    msgID = message.author.id
    if sessions[message.author.id] == None: return
    if message.content.lower().startswith("endsession"):
        save(msgID)
        remove(msgID)
        message.channel.send("Session Ended. Thanks for your contributions.")
    
    if sessions[msgID]["mode"] == "pattern":
        sessions[msgID]["messages"].append(message.content.lower())
    else:
        sessions[msgID]["messages"].append({"message": message.content.lower(), "question": sessions[msgID]["question"]})
    message.react("✅")

    if sessions[msgID]["mode"] == "response":
        dataset = wbjson.ReadToRaw("dataset.json")
        question = random.choice(dataset[sessions[msgID]["type"]]["patterns"])
        embed = discord.Embed(title="**TRAIN**",
            description=f"**Respond to:**\n{question}")
        asyncio.run(message.channel.send(embed=embed))
        sessions[msgID]["question"] = question

def save(id):
    sessData = sessions[id]
    sessData = SimpleNamespace(**sessData)
    if len(sessData) == 0: return

    dataset = wbjson.ReadRaw("dataset.json")
    stats = wbjson.ReadRaw("stats.json")

    for msg in sessData.messages:
        if msg in dataset[sessData.type][sessData.mode + "s"]: return
        stats[sessData.type] += 1;
        dataset[sessData.type][sessData.mode + "s"].append(msg)

        if stats["users"][id] == None:
            stats["users"][id] = 1
        else:
            stats["users"][id] += 1

    wbjson.WriteRaw("dataset.json", dataset)
    wbjson.WriteRaw("stats.json", stats)

def addModel(trainedModel):
    model = trainedModel

def getModel():
    return model