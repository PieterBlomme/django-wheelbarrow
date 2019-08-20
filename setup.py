import setuptools
from django-wheelbarrow import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-wheelbarrow",
    version=__version__,
    author="Pieter Blomme",
    author_email="pieter.blomme@gmail.com",
    description="Helper package to create Django e-commerce sites",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PieterBlomme/django-wheelbarrow",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)