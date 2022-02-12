import asyncio
from functools import partial

async def main():
    print('main start')
    await asyncio.sleep(1)
    print('main 1/2')
    loop.call_soon(partial(print, 'call soon 2'))
    loop.call_later(1, partial(print, 'call later 2'))
    await asyncio.sleep(1)
    print('main end')

print('start')
loop = asyncio.new_event_loop()
loop.call_soon(partial(print, 'call soon 1'))
loop.call_later(1, partial(print, 'call later 1'))
loop.run_until_complete(main())
loop.close()
print('end')
