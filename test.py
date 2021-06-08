from training import trainAI
import asyncio
from training import use

async def do_test():
    await trainAI.train_ai()

asyncio.run(do_test())