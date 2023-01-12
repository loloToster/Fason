from setuptools import setup

with open("README.md") as f:
  readme = f.read()

setup(
  name="fason",
  author="loloToster",
  description="Use json files quicker and easier with this python package!",
  long_description=readme,
  keywords=["python", "json"],
  packages=["fason"]
)
