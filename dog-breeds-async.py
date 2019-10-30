import asyncio

from helpers import afetch


async def fetch_doggos():
    response = await afetch('https://dog.ceo/api/breeds/list/all')
    responses = []
    for breed in response['message'].keys():
        url = f'https://dog.ceo/api/breed/{breed}/images/random'
        responses.append(afetch(url))
    return await asyncio.gather(*responses)

loop = asyncio.get_event_loop()
doggo_responses = loop.run_until_complete(fetch_doggos())
for doggo_response in doggo_responses:
    print(doggo_response['message'])
