import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mkgist",
    version="3.0",
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
    install_requires=[
        "certifi==2017.11.5",
        "chardet==3.0.4",
        "idna==2.6",
        "pyperclip==1.6.0",
        "requests==2.18.4",
        "urllib3==1.22",
    ],
)
