#!/usr/bin/env python3

import os
import re

path = 'recipes'
files = os.listdir(path)

rating1 = []
rating2 = []
rating3 = []
rating4 = []
rating5 = []

for file in files:
    extension = os.path.splitext(file)[-1]
    name = os.path.splitext(file)[0]

    content = open(os.path.join(path, file)).readlines()
    header = content[0]
    rating = content[-1]

    if extension != '.md':
        level = 'WARNING'
        message = 'Incorrect file extension'
        print(f'{level:<15} {name:<30} {message}')

    if header != f'# {name}\n':
        level = 'WARNING'
        message = 'Incorrect name header'
        print(f'{level:<15} {name:<30} {message}')

    if not '## Ingredients\n' in content:
        level = 'WARNING'
        message = 'Incorrect ingredients header'
        print(f'{level:<15} {name:<30} {message}')

    if not '## Instructions\n' in content:
        level = 'WARNING'
        message = 'Incorrect instructions header'
        print(f'{level:<15} {name:<30} {message}')

    if not '## Glassware\n' in content:
        level = 'WARNING'
        message = 'Incorrect glassware header'
        print(f'{level:<15} {name:<30} {message}')

    if not '## Rating\n' in content:
        level = 'WARNING'
        message = 'Incorrect rating header'
        print(f'{level:<15} {name:<30} {message}')

    if not re.match('^- ★[★☆]{4}$', rating):
        level = 'WARNING'
        message = 'Incorrect rating'
        print(f'{level:<15} {name:<30} {message}')

    if re.search('<!--', str(content)):
        level = 'INFO'
        message = 'Contains comments'
        print(f'{level:<15} {name:<30} {message}')

    match rating:
        case "- ★☆☆☆☆":
            rating1.append(name)

        case "- ★★☆☆☆":
            rating2.append(name)

        case "- ★★★☆☆":
            rating3.append(name)

        case "- ★★★★☆":
            rating4.append(name)

        case "- ★★★★★":
            rating5.append(name)

print(f'\nNumber of drinks in total:\n{len(files)}')

print('\nNumber of drinks per rating:')
print(f'★☆☆☆☆\t\t{len(rating1)}\t\t{round(len(rating1) / len(files) * 100, 2)}%')
print(f'★★☆☆☆\t\t{len(rating2)}\t\t{round(len(rating2) / len(files) * 100, 2)}%')
print(f'★★★☆☆\t\t{len(rating3)}\t\t{round(len(rating3) / len(files) * 100, 2)}%')
print(f'★★★★☆\t\t{len(rating4)}\t\t{round(len(rating4) / len(files) * 100, 2)}%')
print(f'★★★★★\t\t{len(rating5)}\t\t{round(len(rating5) / len(files) * 100, 2)}%')
