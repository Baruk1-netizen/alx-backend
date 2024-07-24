# Cache Systems Project

Author: Baruk1-netizen

## Overview

This project involves the creation of different caching systems, each implementing a specific cache replacement policy. The caching systems inherit from a base class, `BaseCaching`, and use a dictionary, `self.cache_data`, for storing the cache items.

## Caching Systems

### 0. Basic Cache

- **Class Name:** `BasicCache`
- **Inheritance:** Inherits from `BaseCaching`
- **Behavior:** 
  - The caching system does not have a limit.
  - **Methods:**
    - `put(self, key, item)`: Assigns the `item` value to the `key` in the `self.cache_data` dictionary. If `key` or `item` is `None`, the method does nothing.
    - `get(self, key)`: Returns the value in `self.cache_data` linked to `key`. If `key` is `None` or does not exist in `self.cache_data`, returns `None`.

### 1. FIFO Cache

- **Class Name:** `FIFOCache`
- **Inheritance:** Inherits from `BaseCaching`
- **Behavior:**
  - Uses First-In-First-Out (FIFO) caching algorithm.
  - **Methods:**
    - `put(self, key, item)`: Adds the `item` to the cache with the given `key`. If the number of items exceeds `BaseCaching.MAX_ITEMS`, it discards the oldest item and prints `DISCARD: <key>` where `<key>` is the key of the discarded item.
    - `get(self, key)`: Returns the value associated with `key`. If `key` is `None` or not present, returns `None`.

### 2. LIFO Cache

- **Class Name:** `LIFOCache`
- **Inheritance:** Inherits from `BaseCaching`
- **Behavior:**
  - Uses Last-In-First-Out (LIFO) caching algorithm.
  - **Methods:**
    - `put(self, key, item)`: Adds the `item` to the cache with the given `key`. If the number of items exceeds `BaseCaching.MAX_ITEMS`, it discards the most recently added item and prints `DISCARD: <key>` where `<key>` is the key of the discarded item.
    - `get(self, key)`: Returns the value associated with `key`. If `key` is `None` or not present, returns `None`.

### 3. LRU Cache

- **Class Name:** `LRUCache`
- **Inheritance:** Inherits from `BaseCaching`
- **Behavior:**
  - Uses Least Recently Used (LRU) caching algorithm.
  - **Methods:**
    - `put(self, key, item)`: Adds the `item` to the cache with the given `key`. If the number of items exceeds `BaseCaching.MAX_ITEMS`, it discards the least recently used item and prints `DISCARD: <key>` where `<key>` is the key of the discarded item.
    - `get(self, key)`: Returns the value associated with `key`. If `key` is `None` or not present, returns `None`.

### 4. MRU Cache

- **Class Name:** `MRUCache`
- **Inheritance:** Inherits from `BaseCaching`
- **Behavior:**
  - Uses Most Recently Used (MRU) caching algorithm.
  - **Methods:**
    - `put(self, key, item)`: Adds the `item` to the cache with the given `key`. If the number of items exceeds `BaseCaching.MAX_ITEMS`, it discards the most recently used item and prints `DISCARD: <key>` where `<key>` is the key of the discarded item.
    - `get(self, key)`: Returns the value associated with `key`. If `key` is `None` or not present, returns `None`.

## Repository Structure

- **GitHub repository:** `alx-backend`
- **Directory:** `0x01-caching`
- **Files:**
  - `0-basic_cache.py`: Contains the implementation of `BasicCache`.
  - `1-fifo_cache.py`: Contains the implementation of `FIFOCache`.
  - `2-lifo_cache.py`: Contains the implementation of `LIFOCache`.
  - `3-lru_cache.py`: Contains the implementation of `LRUCache`.
  - `4-mru_cache.py`: Contains the implementation of `MRUCache`.

## Usage

Each caching system can be tested using corresponding main files provided in the repository. The main files demonstrate the creation of cache instances, adding items to the cache, retrieving items, and the behavior of each caching system when the cache limit is exceeded.

## Example

Here's a quick example of using the `BasicCache`:

```python
#!/usr/bin/python3
""" 0-main """
BasicCache = __import__('0-basic_cache').BasicCache

my_cache = BasicCache()
my_cache.print_cache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.print_cache()
print(my_cache.get("A"))  # Output: Hello
print(my_cache.get("B"))  # Output: World
print(my_cache.get("C"))  # Output: Holberton
print(my_cache.get("D"))  # Output: None
my_cache.print_cache()
```

## License

This project is licensed under the MIT License.

---

For further information, please refer to the project's repository on GitHub.
