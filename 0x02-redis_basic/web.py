#!/usr/bin/env python3
"""This script tracts the live of caches"""
import requests
import redis
from functools import wraps
from typing import Callable


def count_access(method: Callable) -> Callable:
    """This function checks and update or set the cache time"""
    @wraps(method)
    def wrapper(*args, **kwargs) -> str:
        url: str = args[0]
        count_key: str = f"count:{url}"
        cache_key: str = f"cache:{url}"

        access_count: int = redis_client.incr(count_key)

        print(f"Access count for {url}: {access_count}")
        cached_result: bytes = redis_client.get(cache_key)
        if cached_result:
            return cached_result.decode("utf-8")

        result: str = method(*args, **kwargs)
        redis_client.setex(cache_key, 10, result)

        return result
    return wrapper


@count_access
def get_page(url: str) -> str:
    """This function send http requests to the supplied url"""
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    redis_client: redis.Redis = redis.Redis()
    slow_url: str = ("http://slowwly.robertomurray.co.uk"
                     "/delay/1000/url/https://www.example.com")
    print(get_page(slow_url))
    print(get_page(slow_url))

    fast_url: str = ("https://github.com/Dennismwendwa/alx-backend-storage/"
                     "blob/main/0x02-redis_basic/exercise.py")

    print(get_page(fast_url))

    import time
    time.sleep(11)
    print(get_page(slow_url))
