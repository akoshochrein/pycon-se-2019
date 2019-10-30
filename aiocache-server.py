import asyncio

from aiocache import cached
from aiohttp import web
from helpers import afetch


@cached(ttl=10)
async def cached_afetch(url):
    return await afetch(url)


async def handle(request):
    breed = request.match_info.get('breed') or 'labrador'
    image_response = await cached_afetch(f'https://dog.ceo/api/breed/{breed}/images/random')
    return web.Response(
        body=f'<img src="{image_response["message"]}" />',
        content_type='text/html'
    )


app = web.Application()
app.add_routes([
    web.get('/', handle),
    web.get('/{breed}', handle),
])


if __name__ == '__main__':
    web.run_app(app)
