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
        print(f"WARNING: '{name}' has an incorrect filename.")

    if not re.match('^★[★☆]{4}$', rating):
        print(f"WARNING: '{name}' has an incorrect rating.")

    if re.search('<!--', str(content)):
        print(f"WARNING: '{name}' contains comments.")

    if not '## Ingredients\n' in content:
        print(f"WARNING: '{name}' has no ingredients section.")

    if not '## Instructions\n' in content:
        print(f"WARNING: '{name}' has no instructions section.")

    if not '## Glassware\n' in content:
        print(f"WARNING: '{name}' has no glassware section.")

    if not '## Rating\n' in content:
        print(f"WARNING: '{name}' has no rating section.")
