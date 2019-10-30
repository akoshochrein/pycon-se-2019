import trio

from helpers import afetch


async def child1():
    response = await afetch('https://dog.ceo/api/breed/pug/images/random')
    print(response['message'])

async def child2():
    response = await afetch('https://dog.ceo/api/breed/puli/images/random')
    print(response['message'])

async def parent():
    async with trio.open_nursery() as nursery:
        nursery.start_soon(child1)
        nursery.start_soon(child2)

trio.run(parent)
