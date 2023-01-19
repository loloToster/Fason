import pytest
import json
from fason import JsonDb


@pytest.fixture(scope="function")
def sample_dict():
  return {
    "1": "num_value",
    "key": "value",
    "x": {
      "2": {
        "y": True
      },
      "z": None
    },
    "config": {
      "api_key": "QWERTY123",
      "cache": False,
      "version": 10
    },
    "users": [
      {
        "name": "John",
        "age": 31
      },
      {
        "name": "James",
        "age": 42
      },
      {
        "name": "Mary",
        "age": 23
      }
    ]
  }

@pytest.fixture(scope="function")
def dict_db(tmpdir, sample_dict):
  path = tmpdir + "/db.json"

  with open(path, "w") as f:
    json.dump(sample_dict, f)

  db = JsonDb(path)

  return db
