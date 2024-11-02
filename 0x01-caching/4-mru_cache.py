#!/usr/bin/env python3
""" this module implement MRU caching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ this class implement MRU"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """setter method ofr self.cach_data"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                mru, _ = self.cache_data.popitem(last=True)
                print(f"DISCARD: {mru}")

            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

    def get(self, key):
        """getter method"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
