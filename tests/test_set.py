from fason import JsonDb


def test_simple_set(dict_db: JsonDb):
  dict_db.set("test", 123)
  assert dict_db.to_native()["test"] == 123

def test_nested_set(dict_db: JsonDb):
  dict_db.set(["test", "test2"], "456")
  assert dict_db.to_native()["test"]["test2"] == "456"

def test_set_with_non_string_key(dict_db: JsonDb):
  dict_db.set(1, 2)
  assert dict_db.to_native()["1"] == 2

def test_nested_set_with_non_string_key(dict_db: JsonDb):
  dict_db.set([1, 2, 3], "test")
  assert dict_db.to_native()["1"]["2"]["3"] == "test"
