import asyncio
import random


async def print_breed(breed, future):
    await asyncio.sleep(random.randint(1, 4))
    future.set_result(f'{breed}')


def print_done(future):
    print('done')


def print_result(future):
    print(future.result())


breeds = ['labrador', 'golden retriever', 'pug']
futures = [asyncio.Future() for _ in range(len(breeds))]
for index, future in enumerate(futures):
    asyncio.ensure_future(print_breed(breeds[index], future))


loop = asyncio.get_event_loop()
try:
    loop.run_forever()
finally:
    loop.close()
