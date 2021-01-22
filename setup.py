from setuptools import setup, find_packages

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(name="riiid-app",
      version="1.0",
      description="riiid-app",
      packages=find_packages(),
      include_package_data=True,
      install_requires=requirements)