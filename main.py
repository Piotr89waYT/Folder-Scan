# By Frosty

from pathlib import Path

folder_path = Path.cwd()
output_file = Path('dump.txt')

with output_file.open('w', encoding='utf-8') as f:
    for entry in folder_path.rglob('handling.meta'):
        if entry.is_file():
            f.write(str(entry.resolve()) + '\n')



# POSSIBLE TO DO

# Make CMD Ui
# Choose custom path
# Scan all file types and ask which file extension you want?
# Search for specific file