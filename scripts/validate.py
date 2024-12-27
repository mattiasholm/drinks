#!/usr/bin/env python3

import os
import re
import sys

path = '../drinks'
files = os.listdir(path)

failure = False

for file in files:
    name = os.path.splitext(file)[0]
    extension = os.path.splitext(file)[-1]

    content = open(os.path.join(path, file)).readlines()
    header = content[0]
    rating = content[-1]

    if extension != '.md':
        level = 'WARNING'
        message = 'Incorrect file extension'
        failure = True
        print(f'{name:<30} {level:<15} {message}')

    if header != f'# {name}\n':
        level = 'WARNING'
        message = 'Incorrect name header'
        failure = True
        print(f'{name:<30} {level:<15} {message}')

    if '## Ingredients\n' not in content:
        level = 'WARNING'
        message = 'Incorrect ingredients header'
        failure = True
        print(f'{name:<30} {level:<15} {message}')

    if '## Instructions\n' not in content:
        level = 'WARNING'
        message = 'Incorrect instructions header'
        failure = True
        print(f'{name:<30} {level:<15} {message}')

    if '## Glassware\n' not in content:
        level = 'WARNING'
        message = 'Incorrect glassware header'
        failure = True
        print(f'{name:<30} {level:<15} {message}')

    if '## Rating\n' not in content:
        level = 'WARNING'
        message = 'Incorrect rating header'
        failure = True
        print(f'{name:<30} {level:<15} {message}')

    if not re.match('^- ★[★☆]{4}$', rating):
        level = 'WARNING'
        message = 'Incorrect rating'
        failure = True
        print(f'{name:<30} {level:<15} {message}')

    if re.search('<!--', str(content)):
        level = 'INFO'
        message = 'Contains comments'
        failure = True
        print(f'{name:<30} {level:<15} {message}')

if failure:
    sys.exit(2)
