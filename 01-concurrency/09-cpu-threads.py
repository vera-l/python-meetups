import time
from threading import Thread
from functools import partial

from tasks import cpu_task, NUMBERS

start = time.time()

threads = [Thread(target=partial(cpu_task, n)) for n in NUMBERS]
[t.start() for t in threads]
[t.join() for t in threads]

print(time.time() - start, 'sec, for ', len(NUMBERS), ' items')
