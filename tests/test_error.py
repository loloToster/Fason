import pytest
from fason import JsonDb


def test_create_with_invalid_path():
  with pytest.raises(Exception):
    JsonDb("/")

def test_using_non_serializable_value(dict_db: JsonDb):
  class Test(): pass
  
  with pytest.raises(TypeError):
    dict_db.set("x", Test())
