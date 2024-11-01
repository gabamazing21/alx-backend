#!/usr/bin/python3
""" BaseCaching module
"""
from basecaching import BaseCaching


class BasicCache(BaseCaching):
    """basic cache herit from basecatching"""

    def __init__(self):
        """initialize the basiccache class"""
        super().__init__()

    def put(self, key, item):
        """
        setter method
        """
        if (key is None or item is None):
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """getter method"""
        if (key is None or key not in self.cache_data):
            pass
        else:
            return self.cache_data[key]
