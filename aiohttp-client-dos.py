import aiohttp
import asyncio


async def afetch_html(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def bomb(kilotons):
    requests = [afetch_html('http://localhost:8080/nighty') for _ in range(kilotons)]
    return await asyncio.gather(*requests)


loop = asyncio.get_event_loop()
loop.run_until_complete(bomb(10))
