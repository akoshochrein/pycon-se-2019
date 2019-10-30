import asyncio

from aiohttp import web
from helpers import afetch


async def handle(request):
    breed = request.match_info.get('breed') or 'labrador'
    image_response = await afetch(f'https://dog.ceo/api/breed/{breed}/images/random')
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
