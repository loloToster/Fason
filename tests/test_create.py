from fason import JsonDb


def test_create(tmpdir):
  db = JsonDb(tmpdir + "/db.json")
  assert not db._memory_only

def test_create_in_memory():
  db = JsonDb()
  assert db._memory_only
  db = JsonDb(":memory:")
  assert db._memory_only

def test_create_with_exisiting_file(tmpdir):
  path = tmpdir + "/db.json"
  open(path, "w").close()

  db = JsonDb(path)
  assert not db._memory_only
