import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mkgist",
    version="3.4",
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
    license = "MIT",
    scripts=["bin/mkgist"],
    install_requires=[
        "certifi==2019.3.9",
        "chardet==3.0.4",
        "idna==2.8",
        "pyperclip==1.7.0",
        "requests==2.21.0",
        "urllib3==1.25.8",
    ],
)
