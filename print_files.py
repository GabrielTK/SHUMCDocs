import os

for file in os.listdir('guides/industries-101/Slimefun/'):
    title = file.replace('.md', '').replace('-', ' ').title()
    print(f'    * [{title}](guides/industries-101/Slimefun/{file})')