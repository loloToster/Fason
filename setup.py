from setuptools import setup

with open("README.md") as f:
  readme = f.read()

setup(
  name="fason",
  author="loloToster",
  description="Use json files quicker and easier with this python package!",
  long_description=readme,
  long_description_content_type="text/markdown",
  keywords=["python", "json"],
  packages=["fason"]
)
