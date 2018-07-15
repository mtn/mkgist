import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mkgist",
    version="2.0",
    author="Michael Noronha",
    author_email="michaeltnoronha@gmail.com",
    description="A small utility for making gists",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mtn/mkgist",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    scripts=["bin/mkgist"],
)
