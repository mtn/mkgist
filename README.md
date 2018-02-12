# mkgist

A small utility for making gists. When I need to share code snippets online, the formatting always ends up totally messed up when I copy-paste manually. This alleviates that.

## Usage

    mkgist filename [-d "description"] [--secret] [--raw]

The location of the created gist is printed to stdout. Gists are anonymous. Secret gists aren't indexed by search engines, though regular anonymous ones don't seem to be anyways. `[--raw]` returns a link to the raw hosted file, which you can then get with `curl` or `wget`.

Also, it's probably a good idea to have it in the path.
