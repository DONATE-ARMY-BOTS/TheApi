from setuptools import setup, find_packages

def read_requirements():
    try:
        with open("requirements.txt") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

setup(
    name="TheApi",
    version="0.2",
    packages=find_packages(),
    install_requires=read_requirements(),
)