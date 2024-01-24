#!/usr/bin/env python3
"""This script creates a cache class to store redis instances"""
import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def replay(method: Callable) -> None:
    """This function display the history of call of passed functions"""
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"

    inputs = method.__self__._redis.lrange(input_key, 0, -1)
    outputs = method.__self__._redis.lrange(output_key, 0, -1)
    print(f"{method.__qualname__} was called {len(inputs)} times:")

    for args, result in zip(inputs, outputs):
        print(
            (f"{method.__qualname__}{args.decode('utf-8')} "
             f"-> {result.decode('utf-8')}")
            )


def call_history(method: Callable) -> Callable:
    """Records the call history of method in Cache class"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Returns the methods output after increament"""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))

        result = method(self, *args, **kwargs)

        self._redis.rpush(output_key, result)
        return result
    return wrapper


def count_calls(method: Callable) -> Callable:
    """This function counts how many times methods of Cache class are called"""

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """Call the passed method"""
        key = method.__qualname__
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(key)
        result = method(self, *args, **kwargs)
        return result
    return wrapper


class Cache:
    """This are the attributes of the class. Redis"""
    def __init__(self):
        """This is the constructor method of the class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """This method takes a data argument and return string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float, None]:
        """
        This method convents data from redis database to its original type
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> Optional[str]:
        """This method return string"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """This method returns a int"""
        return self.get(key, fn=int)
