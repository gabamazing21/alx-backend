#!/usr/bin/env python3
""" this module implement FIFO caching
"""
from basecaching import BaseCaching


class FIFOCache(BaseCaching):
    """ this class implement FIFO"""
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """setter method ofr self.cach_data"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)

            self.cache_data[key] = item
            self.order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = self.order.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

    def get(self, key):
        """getter method"""
        return self.cache_data.get(key, None)
