#!/usr/bin/env python3
import sys
import os
import plistlib
import json
import argparse
from pathlib import Path

_DEBUG = False


def convert_file(filename):
    global _DEBUG

    if _DEBUG:
        print(f'DEBUG: convert_file: filename = {filename}')

    bn = os.path.splitext(filename)[0]

    if _DEBUG:
        print(f'DEBUG: convert_file: bn = {bn}')

    with open(filename, 'rb') as f:
        profile = plistlib.load(f, fmt=plistlib.FMT_XML)

    jsonfn = ''.join([bn, '.json'])
    if _DEBUG:
        print(f'DEBUG: convert_file: jsonfn = {jsonfn}')

    with open(jsonfn, 'w') as f:
        json.dump(profile, f, indent=4)


def convert_dir(dirname):
    global _DEBUG

    if _DEBUG:
        print(f'DEBUG: convert_file: dirname = {dirname}')

    colorsfns = sorted(dirname.glob('*.itermcolors'))

    if _DEBUG:
        print(f'DEBUG: convert_dir: colorsfns = {colorsfns}')

    for fn in colorsfns:
        convert_file(fn)


def main():
    global _DEBUG
    parser = argparse.ArgumentParser(prog='itermcolors2json.py',
                                     description='Convert itermcolors file to JSON')
    parser.add_argument('-d', '--debug', action='store_true', help='debugging output')
    parser.add_argument('file_or_dir', nargs='*', help="file or directory")
    args = parser.parse_args()

    _DEBUG = args.debug

    if _DEBUG:
        print(f'DEBUG: args = {args}')
        print(f'DEBUG: type(args.file_or_dir) = {type(args.file_or_dir[0])}')

    for ford in args.file_or_dir:
        if Path(ford).exists():
            if _DEBUG:
                print(Path(ford))

            if Path(ford).is_file():
                convert_file(Path(ford))
            elif Path(ford).is_dir():
                convert_dir(Path(ford))
        else:
            print(f'ERROR: {Path(ford)} does not exist')
            parser.print_help()
            sys.exit(1)


if __name__ == '__main__':
    main()
