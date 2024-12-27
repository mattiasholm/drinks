#!/usr/bin/env python3

import os

path = '../drinks'
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
    name = os.path.splitext(file)[0]
    extension = os.path.splitext(file)[-1]

    content = open(os.path.join(path, file)).readlines()
    rating = content[-1]

    ratings[rating.count('★')]['drinks'].append(name)

print(f'Number of drinks:\n{file_count}')

counts = []

for key, value in ratings.items():
    count = len(value['drinks'])
    counts.append(key * count)

average = round(sum(counts) / file_count, 1)
print(f'\nAverage rating:\n{average}')

print('\nDrinks per rating:')

for rating in ratings.values():
    stars = rating['stars']
    count = len(rating['drinks'])
    percentage = round(count / file_count * 100, 1)
    print(f'{stars:<30} {count:<15} {percentage}%')
