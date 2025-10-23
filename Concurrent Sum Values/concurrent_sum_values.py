"""
Concurrent Sum of Values
EN
Given a function fetch(id) that returns {"id": id, "value": int}, 
fetch many ids concurrently and return the total sum of "value". 
If any call fails, skip it.

ES
Dada una función fetch(id) que devuelve {"id": id, "value": int},
obtén varios ids en paralelo y devuelve la suma total de "value".
Si alguna llamada falla, ignórala.

Example:
sum_values([1,2,3], fetch)
"""
from concurrent.futures import ThreadPoolExecutor, as_completed

def sum_values(ids, fetch, max_workers=8):
    total = 0
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        futs = {ex.submit(fetch, i): i for i in ids}
        for fut in as_completed(futs):
            try:
                resp = fut.result()
                total += int(resp["value"])
            except Exception:
                continue
    return total

# demo
def fake_fetch(i):
    return {"id": i, "value": i * 2}

print(sum_values(range(1, 6), fake_fetch))
