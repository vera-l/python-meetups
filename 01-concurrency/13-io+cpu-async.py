import asyncio
import time
from tasks import get_url_non_blocking, cpu_task, URLS, NUMBERS

URLS = URLS[:10]


async def get_url_non_blocking_then_block(url):
    await get_url_non_blocking(url)
    cpu_task(NUMBERS[-3])
    

async def main():
    await asyncio.gather(*[get_url_non_blocking_then_block(url) for url in URLS])
   
start = time.time()
asyncio.run(main())
print(time.time() - start, 'sec, for ', len(URLS), ' items')
