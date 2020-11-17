import os
import asyncio
import time
import concurrent.futures

from tasks import get_url_non_blocking, URLS, cpu_task, NUMBERS

if __name__ == '__main__':

    URLS = URLS[:10]
    pool = concurrent.futures.ProcessPoolExecutor(max_workers=os.cpu_count())


    async def get_url_non_blocking_plus_cpu_or_blocking(url):
        loop = asyncio.get_event_loop()
        await get_url_non_blocking(url)
        await loop.run_in_executor(pool, cpu_task, NUMBERS[-3])


    async def main():
        await asyncio.gather(*[get_url_non_blocking_plus_cpu_or_blocking(url) for url in URLS])

    start = time.time()
    asyncio.run(main())
    print(time.time() - start, 'sec, for ', len(URLS), ' items')
