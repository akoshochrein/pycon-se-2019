import aiohttp
import requests


def fetch(url):
    return requests.get(url).json()


async def afetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
