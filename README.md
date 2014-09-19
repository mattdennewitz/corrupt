# corrupt

Python port of Recyclism's "corrupt" tool.

## Installation

```shell
$ pip install corrupt
```

or, clone this repo and run `python setup.py install` on your own.

## Usage

```shell
Usage: corrupt [OPTIONS]

  Politely, but firmly reconsider byte arrangement from ``input``, render to
  ``output``.

  @param source Path to source image @param output Path to output image
  @param iterations How many times to rethink and rearrange.

Options:
  -s, --source FILENAME       [required]
  -o, --output FILENAME       [required]
  -i, --iterations INTEGER
  -r, --replacements INTEGER  Number of replacements made per iteration.
                              Default: 5.
  -v, --verbose
  --help                      Show this message and exit.
```

Example:

```shell
$ corrupt -s /path/to/input.jpg -o /path/to/output.jpg
```

### Options

- `-s`, Path to input image
- `-o`, Path to corrupted output
- `-i`, Number of corruptions made
- `-r`, Number of byte replacements per corruption
- `-v`, Enable verbose output
