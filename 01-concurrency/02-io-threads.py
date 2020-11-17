import time
from threading import Thread
from functools import partial

from tasks import get_url_blocking, URLS

start = time.time()

threads = [Thread(target=partial(get_url_blocking, url)) for url in URLS]
[t.start() for t in threads]
[t.join() for t in threads]

print(time.time() - start, 'sec, for ', len(URLS), ' items')
