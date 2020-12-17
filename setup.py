from setuptools import setup, find_packages
with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(
    name='Riiid challenge',
    version='1.0',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='Riiid challenge Pipeline',
    install_requires=requirements
)
