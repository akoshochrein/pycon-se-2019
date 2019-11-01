import asyncio

from aiofile import AIOFile
from aiohttp import web
from aiojobs.aiohttp import setup, spawn
from helpers import afetch


async def save_doggo(breed):
    print(f'saving {breed}'...)
    image_response = await afetch(f'https://dog.ceo/api/breed/{breed}/images/random')
    async with AIOFile(f'/tmp/{breed}.txt', 'w+') as afp:
        await afp.write(image_response['message'])
        await afp.fsync()
    print(f'saved {breed}!')


async def handle(request):
    breed = request.match_info.get('breed') or 'labrador'
    await spawn(request, save_doggo(breed))
    return web.Response(text='In progress...')


app = web.Application()
app.add_routes([
    web.get('/', handle),
    web.get('/{breed}', handle),
])
setup(app)


if __name__ == '__main__':
    web.run_app(app)
