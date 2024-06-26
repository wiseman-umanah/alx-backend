#!/usr/bin/env python3
"""Module of a basic caching
System Ops"""
from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """Basic Caching Class

    Methods:
        put -> add data to cache system
        get -> retrieve data from caching system
    """
    def __init__(self):
        super().__init__()
        self.cache_data = {}
        self.freq = defaultdict(int)

    def put(self, key, item):
        """Adds data to cache system"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_freq = min(self.freq.values())
            least_used_keys = [k for k, v in self.freq.items()
                               if v == min_freq]
            lfu_key = least_used_keys[0]
            del self.cache_data[lfu_key]
            del self.freq[lfu_key]
            print("DISCARD:", lfu_key)

        self.cache_data[key] = item
        self.freq[key] = self.freq.get(key, 0) + 1

    def get(self, key):
        """Retrieves data from caching system"""
        if key in self.cache_data:
            self.freq[key] += 1
            return self.cache_data[key]
        return None
