"""
Flatten and Unflatten JSON
EN
Write two functions: flatten() that converts nested dicts into dot-path keys, 
and unflatten() that rebuilds the original nested structure.

ES
Escribe dos funciones: flatten() que convierte diccionarios anidados en claves con punto,
y unflatten() que reconstruye la estructura original.

Example:
flatten({"a":{"b":1}}) → {"a.b": 1}
unflatten({"a.b":1}) → {"a":{"b":1}}
"""
def flatten(d, prefix=""):
    out = {}
    for k, v in d.items():
        key = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            out.update(flatten(v, key))
        else:
            out[key] = v
    return out

def unflatten(d):
    root = {}
    for path, val in d.items():
        cur = root
        parts = path.split(".")
        for p in parts[:-1]:
            if p not in cur or not isinstance(cur[p], dict):
                cur[p] = {}
            cur = cur[p]
        cur[parts[-1]] = val
    return root

print(flatten({"a": {"b": 1}}))
print(unflatten({"a.b": 1}))
