import os
import time
import concurrent.futures

from tasks import get_url_blocking, URLS

start = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=min(32, os.cpu_count() + 4)) as executor:
    executor.map(get_url_blocking, URLS)

print(time.time() - start, 'sec, for ', len(URLS), ' items')
