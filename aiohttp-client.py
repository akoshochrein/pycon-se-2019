import aiohttp
import asyncio


async def afetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def afetch_html(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    # TODO
    pass


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
