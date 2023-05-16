#!/usr/bin/env python3

from gendiff.gendiff import generate_diff
from gendiff.parse_args import parse_args


def main():
    file1, file2, formatter = parse_args()
    print(generate_diff(file1, file2, formatter))


if __name__ == '__main__':
    main()
