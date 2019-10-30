import asyncio


async def print_dog(breed):
    await asyncio.sleep(1.0)
    print(breed)

async def print_dogs(*breeds):
    for breed in breeds:
        await print_dog(breed)

loop = asyncio.get_event_loop()
loop.run_until_complete(
    print_dogs('labrador', 'golden retriever', 'pug')
)
