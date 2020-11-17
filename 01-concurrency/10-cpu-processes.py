import time
from multiprocessing import Process
from functools import partial

from tasks import cpu_task, NUMBERS


if __name__ == '__main__':
    start = time.time()

    processes = [Process(target=partial(cpu_task, number)) for number in NUMBERS]
    [p.start() for p in processes]
    [p.join() for p in processes]
    [p.close() for p in processes]

    print(time.time() - start, 'sec, for ', len(NUMBERS), ' items')
