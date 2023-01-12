import pytest
import json
from fason import JsonDb


@pytest.fixture(scope="function")
def sample_data():
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
def json_db(tmpdir, sample_data):
  path = tmpdir + "/db.json"

  with open(path, "w") as f:
    json.dump(sample_data, f)

  db = JsonDb(path)

  return db
