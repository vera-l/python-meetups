import os
import time
import concurrent.futures

from tasks import cpu_task, NUMBERS

start = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=min(32, os.cpu_count() + 4)) as executor:
    executor.map(cpu_task, NUMBERS)

print(time.time() - start, 'sec, for ', len(NUMBERS), ' items')
