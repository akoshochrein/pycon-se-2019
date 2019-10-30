import httpx


async def afetch(url):
    async with httpx.AsyncClient() as client:
        return await client.get(url)
