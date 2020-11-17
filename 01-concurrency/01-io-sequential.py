import time

from tasks import get_url_blocking, URLS

start = time.time()

for url in URLS:
    get_url_blocking(url)
    
print(time.time() - start, 'sec, for ', len(URLS), ' items')
