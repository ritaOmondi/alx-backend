# Caching System

This repository contains a simple caching system implemented in Python, inheriting from a base class `BaseCaching`.

## Features

* **Basic caching:** Provides a dictionary-based cache for storing and retrieving values.
* **Limited capacity:** The cache has a maximum size defined by `BaseCaching.MAX_ITEMS`.
* **Least Recently Used (LRU) eviction:** When the cache is full, the least recently used item is evicted to make space for new items.

## Usage

```python
from basic_cache import BasicCache

# Create a cache instance
cache = BasicCache()

# Store values in the cache
cache.put("key1", "value1")
cache.put("key2", "value2")
cache.put("key3", "value3")
cache.put("key4", "value4")

# Retrieve values from the cache
value1 = cache.get("key1")
value2 = cache.get("key2")

# Add a new item, causing the least recently used item to be evicted
cache.put("key5", "value5")

# The least recently used item ("key1") is evicted
print(cache.get("key1"))  # Output: None
