from training import trainAI

names = ["trainmodel", "tftrain"]
async def execute(env):
    message = env.message
    message.channel.send("Training Tensorflow Model.")
    model = await trainAI.train_ai()
    message.channel.send("Finished Training Model")