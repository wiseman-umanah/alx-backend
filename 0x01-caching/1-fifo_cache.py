#!/usr/bin/env python3
"""Module of a basic caching
System Ops"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Basic Caching Class

    Methods:
        put -> add data to cache system
        get -> retrieve data from caching system
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Adds data to cache system"""
        if key is not None or item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            tem = [x for x in self.cache_data]
            del self.cache_data[tem[0]]
            print("DISCARD:", tem[0])

    def get(self, key):
        """Retrieves data from caching system"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
