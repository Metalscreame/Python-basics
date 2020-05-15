import asyncio


async def hi_world():
    print('hello')
    await asyncio.sleep(1)
    print('world')


async def hi():
    print('hi')
    await asyncio.sleep(2)
    print('Roman')


asyncio.run(hi_world())
asyncio.run(hi())
