#!/usr/bin/env python3
"""Module of a basic caching
System Ops"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic Caching Class

    Methods:
        put -> add data to cache system
        get -> retrieve data from caching system
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Adds data to cache system"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves data from caching system"""
        return self.cache_data.get(key, None)
