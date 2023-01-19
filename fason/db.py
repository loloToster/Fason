import json
from typing import Union

class JsonObject:
  def __init__(self, db, data = None):
    self._db = db
    data = data if data else {}

    for k, v in data.items():
      data[k] = JsonObject(self._db, v) if isinstance(v, dict) else v

    self.data = data

  def get(self, keys: Union[str, list[str]]):
    if type(keys) == list:
      prev = self

      for key in keys:
        key = str(key)
        if isinstance(prev, JsonObject):
          prev = prev.get(key)
        else:
          return None
          
      return prev
    else:
      key = str(keys)
      return self.data.get(key, None)

  def set(self, keys: Union[str, list[str]], value):
    if isinstance(value, dict):
      value = JsonObject(self._db, value)

    if type(keys) == list:
      last_key = str(keys.pop())
      prev = self

      for key in keys:
        key = str(key)
        val = prev.get(key)
        if isinstance(val, JsonObject):
          prev = val
        else:
          prev = prev.set(key, {})

      return prev.set(last_key, value)
    else:
      keys = str(keys)
      self.data[keys] = value
      self._db.save()
      return value


  def to_native(self):
    parsed = {}

    for k, v in self.data.items():
      parsed[k] = v.to_native() if isinstance(v, JsonObject) else v

    return parsed


class JsonDb(JsonObject):
  _path: str
  _memory_only: bool

  def __init__(self, path: str = ""):
    self._path = path
    self._memory_only = not path or path == ":memory:"
    
    if self._memory_only:
      super().__init__(db=self)
      return

    open(path, "a+").close() # create the file if it does not exist

    with open(path, "r") as f:
      try:
        super().__init__(db=self, data=json.load(f))
      except:
        super().__init__(db=self)
        self.save()


  def save(self):
    if self._memory_only:
      return

    with open(self._path, "w+") as f:
      json.dump(self.to_native(), f, indent=2)
