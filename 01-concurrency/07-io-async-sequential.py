import asyncio
import time
from tasks import get_url_non_blocking, URLS


async def main():
    for url in URLS:
        await get_url_non_blocking(url)

start = time.time()  
asyncio.run(main())
print(time.time() - start, 'sec, for ', len(URLS), ' items')
