# mkgist

A small utility for making gists. When I need to share code snippets online, the formatting always ends up totally messed up when I copy-paste manually. This alleviates that.

## Setup

For general use, it's a good idea to keep it somewhere in your path. Because the endpoint requires authentication, you should create a JSON file with your credentials called `.mkgist.conf` at the home directory. For example,

```
{
  "username": "user",
  "password": "password"
}
```

To install dependencies, run `pip install -r requirements.txt` after installing.

## Usage

    mkgist filenames [-d "description"] [--public] [--raw] [--nocopy]

The location of the created gist is printed to stdout. Gists are secret by default, but can be made public with `--public`. Secret gists aren't indexed by search engines. `--raw` returns a link to the raw hosted file, which you can then get with `curl` or `wget`. By default, the URL of the created Gist is copied to the clipboard. `--nocopy` prints this to stdout instead, preserving the clipboard.
