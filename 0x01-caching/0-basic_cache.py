#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """basic cache herit from basecatching"""
    def __init__(self):
        """
        init my class"""
        super().__init__()

    def put(self, key, item):
        """
        setter method
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """getter method"""
        return self.cache_data.get(key, None)
