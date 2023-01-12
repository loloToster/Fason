from fason import JsonDb


def test_simple_set(json_db: JsonDb):
  json_db.set("test", 123)
  assert json_db.to_dict()["test"] == 123

def test_nested_set(json_db: JsonDb):
  json_db.set(["test", "test2"], "456")
  assert json_db.to_dict()["test"]["test2"] == "456"

def test_set_with_non_string_key(json_db: JsonDb):
  json_db.set(1, 2)
  assert json_db.to_dict()["1"] == 2

def test_nested_set_with_non_string_key(json_db: JsonDb):
  json_db.set([1, 2, 3], "test")
  assert json_db.to_dict()["1"]["2"]["3"] == "test"
