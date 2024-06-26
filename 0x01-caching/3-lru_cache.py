#!/usr/bin/env python3
"""Module of a basic caching
System Ops"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Basic Caching Class

    Methods:
        put -> add data to cache system
        get -> retrieve data from caching system
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds data to cache system"""
        if key is not None or item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                val = self.cache_data.popitem(last=False)
                print("DISCARD:", val[0])
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves data from caching system"""
        if key in self.cache_data:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return value
        return None
