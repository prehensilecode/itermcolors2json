#!/usr/bin/env python3
import sys
import os
import plistlib
import json
import argparse

_DEBUG = True

def main():
    global _DEBUG
    parser = argparse.ArgumentParser(prog='itermcolors2json.py',
                                     description='Convert itermcolors file to JSON')
    parser.add_argument('-d', '--debug', action='store_true', help='debugging output')
    args = parser.parse_args()

    _DEBUG = args.debug

    if _DEBUG:
        print(f'DEBUG: args = {args}')

    with open('Neopolitan.itermcolors', 'rb') as f:
        foobar = plistlib.load(f, fmt=plistlib.FMT_XML)

    with open('Foobar.json', 'w') as f:
        json.dump(foobar, f, indent=4)


if __name__ == '__main__':
    main()
