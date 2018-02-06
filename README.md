# mkgist

A small utility for making gists. When I need to share code snippets online, the formatting always ends up totally messed up when I copy-paste manually. This alleviates that.

## Usage

    mkgist filename [-d "description"] [--secret]

The location of the created gist is printed to stdout. Gists are anonymous. Secret gists aren't indexed by search engines, though it's not documented whether regular anonymous ones are to begin with anyways.

Also, it's probably a good idea to have it in the path.
