"""
In-Memory Task API
EN
Create a simple in-memory task manager with CRUD operations.

ES
Crea un gestor de tareas en memoria con operaciones CRUD.

Example:
t = TaskStore()
t.create("Read book")
t.update(1, done=True)
t.list_(done=True)
"""
class TaskStore:
    def __init__(self):
        self._data = {}
        self._next = 1

    def create(self, title):
        t = {"id": self._next, "title": title, "done": False}
        self._data[self._next] = t
        self._next += 1
        return t.copy()

    def get(self, id_):
        t = self._data.get(id_)
        return t.copy() if t else None

    def update(self, id_, **fields):
        t = self._data.get(id_)
        if not t:
            return None
        for k in ("title", "done"):
            if k in fields:
                t[k] = fields[k]
        return t.copy()

    def delete(self, id_):
        return self._data.pop(id_, None) is not None

    def list_(self, done=None):
        vals = list(self._data.values())
        if done is None:
            return [v.copy() for v in vals]
        return [v.copy() for v in vals if v["done"] is done]

store = TaskStore()
store.create("Read book")
store.update(1, done=True)
print(store.list_(done=True))
