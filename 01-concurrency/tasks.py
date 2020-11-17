import requests
import httpx


URLS = [
    'http://www.yahoo.com',
    'http://www.python.org',
    'http://www.pypy.org',
    'http://www.perl.org',
    'http://www.cisco.com',
    'http://www.twitter.com',
    'http://youtube.com',
    'http://google.com',
    'http://github.com',
    'http://yandex.ru',
] * 3

NUMBERS = list(range(28, 35, 1)) * 3


def get_url_blocking(url):
    requests.get(url)
    print(url, ' done')


async def get_url_non_blocking(url):
    print(url, ' start')
    async with httpx.AsyncClient() as client:
        await client.get(url)
        print(url, ' done async')


def _fib(n):
    if n <= 2:
        return 1
    else:
        return _fib(n-1) + _fib(n-2)


def cpu_task(n):
    f = _fib(n)
    print(f'fib({n}) is {f}')
