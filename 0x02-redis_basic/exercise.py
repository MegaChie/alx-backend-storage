#!/usr/bin/env python3
"""Task 0"""
import uuid
from typing import Callable, Optional, Union
import redis


class Cache:
    """A cache class named Cache"""

    def __init__(self) -> None:
        """Initilize the class"""
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Returns the randomly generated key used to store the data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float, None]:
        """Convert the data back to the desired format and returns it"""
        res = self._redis.get(key)
        if res and fn:
            res = fn(res)
        return res

    def get_str(self, key: str) -> str:
        """Convert into string"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """Convert into integer"""
        return self.get(key, int)
