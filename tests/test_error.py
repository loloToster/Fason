import pytest
from fason import JsonDb


def test_create_with_invalid_path():
  with pytest.raises(Exception):
    JsonDb("/")

def test_using_non_serializable_value(json_db: JsonDb):
  class Test(): pass
  
  with pytest.raises(TypeError):
    json_db.set("x", Test())
