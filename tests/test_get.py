from fason import JsonDb


def test_simple_get(dict_db: JsonDb):
  assert dict_db.get("key") == "value"

def test_nested_get(dict_db: JsonDb):
  assert dict_db.get(["config", "api_key"]) == "QWERTY123"

def test_get_with_non_string_key(dict_db: JsonDb):
  assert dict_db.get(1) == "num_value"

def test_nested_get_with_non_string_key(dict_db: JsonDb):
  assert dict_db.get(["x", 2, "y"]) is True

def test_get_non_existing(dict_db: JsonDb):
  assert dict_db.get(["x", "y", "z"]) is None

def test_get_dict(dict_db: JsonDb, sample_dict: dict):
  assert dict_db.to_native() == sample_dict
