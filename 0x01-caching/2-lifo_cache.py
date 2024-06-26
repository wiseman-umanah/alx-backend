#!/usr/bin/env python3
"""Module of a basic caching
System Ops"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
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
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            val = self.cache_data.popitem()
            print("DISCARD:", val[0])
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves data from caching system"""
        return self.cache_data.get(key, None)
