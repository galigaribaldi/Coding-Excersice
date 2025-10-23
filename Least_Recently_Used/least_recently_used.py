"""
Least Recently Used (LRU) Cache
EN
Implement an LRU cache with get() and put() methods, keeping most recently used items.

ES
Implementa una caché LRU con métodos get() y put(), conservando los elementos más usados recientemente.

Example:
cache = LRU(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1) → 1
cache.put(3, 3) → evicts key 2
"""
from collections import OrderedDict

class LRU:
    def __init__(self, cap):
        self.cap = cap
        self.d = OrderedDict()

    def get(self, key):
        if key not in self.d:
            return None
        self.d.move_to_end(key)
        return self.d[key]

    def put(self, key, val):
        if key in self.d:
            self.d.move_to_end(key)
        self.d[key] = val
        if len(self.d) > self.cap:
            self.d.popitem(last=False)

cache = LRU(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
