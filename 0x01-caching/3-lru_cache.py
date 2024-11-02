#!/usr/bin/env python3
""" this module implement LRU caching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ this class implement LRU"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """setter method ofr self.cach_data"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)

            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                l_r_u_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {l_r_u_key}")

    def get(self, key):
        """getter method"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
