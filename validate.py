#!/usr/bin/env python3

import os
import re

path = 'recipes'
files = os.listdir(path)

print(f'Number of drinks: {len(files)}\n')

for file in files:
    file_name = os.path.splitext(file)[0]
    content = open(os.path.join(path, file)).readlines()

    name = content[0].replace('# ', '').strip('\n')
    rating = content[-1].replace('- ', '')

    if file_name != name:
        print(f"WARNING: Filename '{file_name}' does not match '{name}'.")

    regex = '^★[★☆]{4}$'

    if not re.match(regex, rating):
        print(f"WARNING: Rating for '{name}' does not match regex '{regex}'.")

    if not '## Ingredients:\n' in content:
        print(f"WARNING: Ingredients section missing from '{name}'")

    if not '## Instructions:\n' in content:
        print(f"WARNING: Instructions section missing from '{name}'")

    if not '## Glassware:\n' in content:
        print(f"WARNING: Glassware section missing from '{name}'")

    if not '## Rating:\n' in content:
        print(f"WARNING: Rating section missing from '{name}'")
