### Hexlet tests and linter status:
[![Actions Status](https://github.com/jespy666/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/jespy666/python-project-50/actions)
[![Check](https://github.com/jespy666/python-project-50/actions/workflows/check.yml/badge.svg)](https://github.com/jespy666/python-project-50/actions/workflows/check.yml)  
[![Maintainability](https://api.codeclimate.com/v1/badges/be122415f46c4c38bfd1/maintainability)](https://codeclimate.com/github/jespy666/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/be122415f46c4c38bfd1/test_coverage)](https://codeclimate.com/github/jespy666/python-project-50/test_coverage)
# Utility compares two files and shows the difference between them.
### Supported files extension:
* ***json***
* ***yaml/yml***
### Supported output formatters:
* ***'stylish'***
* ***'plain'***
* ***'json'***
### Install:
1. `git clone git@github.com:jespy666/python-project-50.git`
2. `make install`
3. `make package-install`
### Usage:
`gendiff [-h] [-f FORMAT] first_file second_file`
[![asciicast](https://asciinema.org/a/584063.svg)](https://asciinema.org/a/584063)
### Examples:
#### With two simples files. Formatter: 'stylish'.
[![asciicast](https://asciinema.org/a/584058.svg)](https://asciinema.org/a/584058)  
#### With two nested files. Formatter: 'stylish'.
[![asciicast](https://asciinema.org/a/584060.svg)](https://asciinema.org/a/584060)  
#### With two nested files. Formatter: 'plain'.
[![asciicast](https://asciinema.org/a/584061.svg)](https://asciinema.org/a/584061)  
#### With two nested files. Formatter: 'json'.
[![asciicast](https://asciinema.org/a/584062.svg)](https://asciinema.org/a/584062)
