#!/usr/bin/env python3

import os
import re

path = 'recipes'
files = os.listdir(path)
file_count = len(files)

ratings = {
    1: {
        'stars': '★☆☆☆☆',
        'drinks': []
    },
    2: {
        'stars': '★★☆☆☆',
        'drinks': []
    },
    3: {
        'stars': '★★★☆☆',
        'drinks': []
    },
    4: {
        'stars': '★★★★☆',
        'drinks': []
    },
    5: {
        'stars': '★★★★★',
        'drinks': []
    }
}

for file in files:
    extension = os.path.splitext(file)[-1]
    name = os.path.splitext(file)[0]

    content = open(os.path.join(path, file)).readlines()
    header = content[0]
    rating = content[-1]

    if extension != '.md':
        level = 'WARNING'
        message = 'Incorrect file extension'
        print(f'{name:<30} {level:<15} {message}')

    if header != f'# {name}\n':
        level = 'WARNING'
        message = 'Incorrect name header'
        print(f'{name:<30} {level:<15} {message}')

    if not '## Ingredients\n' in content:
        level = 'WARNING'
        message = 'Incorrect ingredients header'
        print(f'{name:<30} {level:<15} {message}')

    if not '## Instructions\n' in content:
        level = 'WARNING'
        message = 'Incorrect instructions header'
        print(f'{name:<30} {level:<15} {message}')

    if not '## Glassware\n' in content:
        level = 'WARNING'
        message = 'Incorrect glassware header'
        print(f'{name:<30} {level:<15} {message}')

    if not '## Rating\n' in content:
        level = 'WARNING'
        message = 'Incorrect rating header'
        print(f'{name:<30} {level:<15} {message}')

    if not re.match('^- ★[★☆]{4}$', rating):
        level = 'WARNING'
        message = 'Incorrect rating'
        print(f'{name:<30} {level:<15} {message}')

    if re.search('<!--', str(content)):
        level = 'INFO'
        message = 'Contains comments'
        print(f'{name:<30} {level:<15} {message}')

    ratings[rating.count('★')]['drinks'].append(name)

print(f'\nNumber of drinks in total:\n{file_count}')

print('\nNumber of drinks per rating:')

values = []

for key, rating in ratings.items():
    stars = rating['stars']
    count = len(rating['drinks'])
    percentage = round(count / file_count * 100, 2)
    values.append(key * count)
    print(f'{stars:<30} {count:<15} {percentage}%')

average = round(sum(values) / file_count, 2)
print(f'\nAverage rating:\n{average}')
