from training import session
import asyncio
import discord
import tensorflow as tf
import time
import config
from training import use

lastcommand = 0

names = ["respond", "test"]
async def execute(env):
    message = env.message
    args = env.args
    model = session.getModel()
    if model == None:
        model = tf.keras.models.load_model(config.MODEL_FILEPATH)
        session.addModel(model)
    
    if args[0] in names or args[0] == "<@562332508042035231>":
        phrase = " ".join(args[1:])
    else:
        phrase = " ".join(args)

    if phrase == " " or phrase == None:
        errorEmbed = discord.Embed(title="**ERROR**",
            description="Please specify a phrase to test.")
        await message.channel.send(embed=errorEmbed)

    # if time.time() - session.lastcommand < 100:
    #     errorEmbed = discord.Embed(title="**SENSORY OVERLOAD**",
    #         description="Please send messages slowly.")
    #     await message.channel.send(embed=errorEmbed)
    
    # session.lastcommand = time.time()

    async with message.channel.typing():
        data = [{"message": phrase}]
        sentences = list(map(lambda i: i["message"].lower(), data))
        xPredict = use.embed(sentences)
        prediction = model.predict(xPredict, batch_size=None, verbose=0, steps=None, callbacks=None, max_queue_size=10, workers=1, use_multiprocessing=False)
    
    predicted = ""
    pList = prediction.tolist()[0]
    likeliest = max(pList)
    if pList[0] == likeliest:
        predicted = "Greeting"
    elif pList[1] == likeliest:
        predicted = "Goodbye"
    elif pList[2] == likeliest:
        predicted = "Insult"
    elif pList[3] == likeliest:
        predicted = "Compliment"

    embed = discord.Embed(title="**PREDICTION**",
            description=f"I predict that this statement is a {predicted}")
    await message.channel.send(embed=embed)
        
