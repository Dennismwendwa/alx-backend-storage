#!/usr/bin/env python3
"""This script tracts the live of caches"""
import requests
import redis
from functools import wraps
from typing import Callable


redis_client = redis.Redis()


def count_access(method: Callable) -> Callable:
    """This function checks and update or set the cache time"""
    @wraps(method)
    def wrapper(url) -> str:
        count_key: str = f"count:{url}"
        result_key: str = f"cache:{url}"

        redis_client.incr(count_key)

        result = redis_client.get(result_key)
        if result:
            return result.decode("utf-8")
        result = method(url)
        redis_client.set(count_key, 0)
        redis_client.setex(result_key, 10, result)

        return result
    return wrapper


@count_access
def get_page(url: str) -> str:
    """This function send http requests to the supplied url"""
    response = requests.get(url)
    return response.text
