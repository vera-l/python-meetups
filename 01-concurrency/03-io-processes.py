import time
from multiprocessing import Process
from functools import partial

from tasks import get_url_blocking, URLS

if __name__ == '__main__':
    start = time.time()

    processes = [Process(target=partial(get_url_blocking, url)) for url in URLS]
    [p.start() for p in processes]
    [p.join() for p in processes]
    [p.close() for p in processes]

    print(time.time() - start, 'sec, for ', len(URLS), ' items')
