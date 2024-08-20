#!/usr/bin/env python3
"""
This module implements a simple caching system using a dictionary.

This module provides a basic implementation of a cache. The cache is a dictionary
that stores key-value pairs. The `get` method retrieves a value from the cache
if it exists. Otherwise, it calls the provided function to calculate the value
and stores it in the cache before returning it.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A simple caching system using a dictionary.

    This class inherits from `BaseCaching` and provides a basic implementation
    of a cache using a dictionary. It allows storing and retrieving values
    based on keys.
    """

    def put(self, key, item):
        """
        Add an item in the cache.

        If the key already exists in the cache, it is overwritten. If the cache
        is full, the least recently used item is evicted to make space for the
        new item.

        Args:
            key (any): The key to store.
            item (any): The value to store.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key.

        If the key exists in the cache, the corresponding value is returned.
        Otherwise, `None` is returned.

        Args:
            key (any): The key to retrieve.

        Returns:
            any: The value associated with the key, or `None` if the key is not
            found.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
