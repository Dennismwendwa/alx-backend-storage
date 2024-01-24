#!/usr/bin/env python3
"""This script creates a cache class to store redis instances"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """This are the attributes of the class. Redis"""
    def __init__(self):
        """This is the constructor method of the class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

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
