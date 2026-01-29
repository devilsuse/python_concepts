import asyncio

async def nested():
    return 42
    #print('async nested')

def non_async_nested():
    #return 42
    print('non_async_nested')

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested()

    #non_async_nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

asyncio.run(main())