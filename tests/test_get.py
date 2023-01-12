from fason import JsonDb


def test_simple_get(json_db: JsonDb):
  assert json_db.get("key") == "value"

def test_nested_get(json_db: JsonDb):
  assert json_db.get(["config", "api_key"]) == "QWERTY123"

def test_get_with_non_string_key(json_db: JsonDb):
  assert json_db.get(1) == "num_value"

def test_nested_get_with_non_string_key(json_db: JsonDb):
  assert json_db.get(["x", 2, "y"]) is True

def test_get_non_existing(json_db: JsonDb):
  assert json_db.get(["x", "y", "z"]) is None

def test_get_dict(json_db: JsonDb, sample_data: dict):
  assert json_db.to_dict() == sample_data
