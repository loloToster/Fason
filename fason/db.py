import json
from typing import Union

class JsonObject:
    def __init__(self, db, data=None):
        self.db = db
        data = data if data else {}

        for k, v in data.items():
            data[k] = JsonObject(self.db, v) if isinstance(v, dict) else v

        self.data = data

    def get(self, keys: Union[str, list]):
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

    def set(self, keys: Union[str, list], value):
        if isinstance(value, dict):
            value = JsonObject(self.db, value)

        if type(keys) == list:
            lastKey = str(keys.pop())
            prev = self

            for key in keys:
                key = str(key)
                val = prev.get(key)
                if isinstance(val, JsonObject):
                    prev = val
                else:
                    prev = prev.set(key, {})

            return prev.set(lastKey, value)
        else:
            keys = str(keys)
            self.data[keys] = value
            self.db.save()
            return value


    def toDict(self):
        parsed = {}

        for k, v in self.data.items():
            parsed[k] = v.toDict() if isinstance(v, JsonObject) else v

        return parsed


class JsonDb(JsonObject):
    def __init__(self, path: str = ""):
        self.path = path
        self.memoryOnly = not path or path == ":memory:"
        
        if self.memoryOnly:
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
        if self.memoryOnly:
            return

        with open(self.path, "w+") as f:
            json.dump(self.toDict(), f, indent=2)
