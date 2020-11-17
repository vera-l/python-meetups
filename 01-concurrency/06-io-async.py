import asyncio
import time
from tasks import get_url_non_blocking, URLS


async def main():
    start = time.time()
    await asyncio.gather(*[get_url_non_blocking(url) for url in URLS])
    print(time.time() - start, 'sec, for ', len(URLS), ' items')
    
asyncio.run(main())
