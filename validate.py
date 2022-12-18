#!/usr/bin/env python3

import os
import re

path = 'recipes'
files = os.listdir(path)

print(f'Number of drinks: {len(files)}\n')

for file in files:
    file_name = os.path.splitext(file)[0]
    content = open(os.path.join(path, file)).readlines()
    header = content[0]
    rating = content[-1]

    if header != f'# {file_name}\n':
        level = 'WARNING'
        message = 'Incorrect name header'
        print(f'{level:<15} {file_name:<30} {message}')

    if not '## Ingredients\n' in content:
        level = 'WARNING'
        message = 'Incorrect ingredients header'
        print(f'{level:<15} {file_name:<30} {message}')

    if not '## Instructions\n' in content:
        level = 'WARNING'
        message = 'Incorrect instructions header'
        print(f'{level:<15} {file_name:<30} {message}')

    if not '## Glassware\n' in content:
        level = 'WARNING'
        message = 'Incorrect glassware header'
        print(f'{level:<15} {file_name:<30} {message}')

    if not '## Rating\n' in content:
        level = 'WARNING'
        message = 'Incorrect rating header'
        print(f'{level:<15} {file_name:<30} {message}')

    if not re.match('^- ★[★☆]{4}$', rating):
        level = 'WARNING'
        message = 'Incorrect rating'
        print(f'{level:<15} {file_name:<30} {message}')

    if re.search('<!--', str(content)):
        level = 'INFO'
        message = 'Contains comments'
        print(f'{level:<15} {file_name:<30} {message}')
