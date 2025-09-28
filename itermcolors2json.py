#!/usr/bin/env python3
import sys
import os
import plistlib
import json
import argparse
from pathlib import Path

_DEBUG = True


def convert_file(filename):
    pass


def convert_dir(dirname):
    pass


def main():
    global _DEBUG
    parser = argparse.ArgumentParser(prog='itermcolors2json.py',
                                     description='Convert itermcolors file to JSON')
    parser.add_argument('-d', '--debug', action='store_true', help='debugging output')
    parser.add_argument('file_or_dir', nargs='*')
    args = parser.parse_args()

    _DEBUG = args.debug

    if _DEBUG:
        print(f'DEBUG: args = {args}')
        print(f'DEBUG: type(args.file_or_dir) = {type(args.file_or_dir[0])}')

    for ford in args.file_or_dir:
        if Path(ford).exists():
            print(Path(ford))
            print(Path(ford).is_file())
            print(Path(ford).is_dir())

    with open('Neopolitan.itermcolors', 'rb') as f:
        foobar = plistlib.load(f, fmt=plistlib.FMT_XML)

    with open('Foobar.json', 'w') as f:
        json.dump(foobar, f, indent=4)


if __name__ == '__main__':
    main()
