from setuptools import setup, find_packages

setup(
    name="automata_library",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Abbas Ali",
    author_email="abbasali1214313@gmail.com",
    description="A Python library for Automata Theory and Formal Languages",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AliOding12/automata_library",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)