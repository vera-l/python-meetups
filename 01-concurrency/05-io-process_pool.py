import os
import time
# from multiprocessing import Pool
import concurrent.futures

from tasks import get_url_blocking, URLS

if __name__ == '__main__':
    start = time.time()

    """
    with Pool(processes=10) as pool:
        pool.map(get_url_blocking, URLS)
    """

    with concurrent.futures.ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
        executor.map(get_url_blocking, URLS)

    print(time.time() - start, 'sec, for ', len(URLS), ' items')
