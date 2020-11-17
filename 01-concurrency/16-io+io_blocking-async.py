import asyncio
import time
from tasks import get_url_non_blocking, get_url_blocking, URLS

URLS = URLS[:20]


async def get_url_non_blocking_then_block(url):
    await get_url_non_blocking(url)
    get_url_blocking(url)
    

async def main():
    await asyncio.gather(*[get_url_non_blocking_then_block(url) for url in URLS])
   
start = time.time()
asyncio.run(main())
print(time.time() - start, 'sec, for ', len(URLS), ' items')
