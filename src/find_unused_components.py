#!/usr/bin/env python
from __future__ import print_function

import argparse
import glob
from os.path import exists
import re


PATTERN = re.compile(r'^import ([A-Z].+) from .+;$', flags=re.M)


def convert_camel_to_kebab(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1-\2', s1).lower()


def count_imports_usage(file_path, ignore=()):
    result = {}
    if not ignore:
        ignore = ('Vue', 'Mixin')

    with open(file_path) as f:
        lines = f.read()
        imports = PATTERN.findall(lines)

        for i in imports:
            if any(ignr in i for ignr in ignore):
                continue

            result[i] = lines.count('<{}'.format(i))
            result[i] += lines.count('<{}'.format(i.lower()))
            result[i] += lines.count('<{}'.format(convert_camel_to_kebab(i)))

    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('path', metavar='DIR', type=str, help='path to directory to look in')

    args = parser.parse_args()
    path = args.path

    if not exists(path):
        print('Path "{}" does not exist'.format(path))
        exit()

    must_fail = False
    for filename in glob.iglob('{}/**/*.vue'.format(path), recursive=True):
        counts = count_imports_usage(filename)
        # print(f'{filename}: {counts}')
        for i in counts:
            if counts[i] == 0:
                must_fail = True
                print('{} component "{}" is not used'.format(filename, i))

    if must_fail:
        exit(1)
