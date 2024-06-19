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
