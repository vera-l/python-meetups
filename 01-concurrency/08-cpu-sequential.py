import time

from tasks import cpu_task, NUMBERS

start = time.time()

for n in NUMBERS:
    cpu_task(n)
    
print(time.time() - start, 'sec, for ', len(NUMBERS), ' items')
