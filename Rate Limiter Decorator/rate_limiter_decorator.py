"""
Rate Limiter Decorator
EN
Create a decorator that limits the number of function calls per minute. 
If the limit is exceeded, raise a RuntimeError.

ES
Crea un decorador que limite el número de llamadas a una función por minuto.
Si se excede el límite, lanza un RuntimeError.

Example:
@rate_limit(3)
def test(): print("ok")
"""
import time
from collections import deque
from functools import wraps

def rate_limit(k):
    def deco(fn):
        hits = deque()
        @wraps(fn)
        def wrapper(*args, **kwargs):
            now = time.time()
            while hits and now - hits[0] > 60:
                hits.popleft()
            if len(hits) >= k:
                raise RuntimeError("Rate limit exceeded")
            hits.append(now)
            return fn(*args, **kwargs)
        return wrapper
    return deco

@rate_limit(3)
def hello():
    print("Hello!")

for _ in range(3):
    hello()
# hello()  # 4th call within 60s → RuntimeError
