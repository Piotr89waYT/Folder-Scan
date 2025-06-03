# By Frosty

import os
from pathlib import Path
import shutil
# CMD Ui
def disclaimer():
    os.system('cls')
    print('''
     ____  _          _       _                     
    |  _ \(_)___  ___| | __ _(_)_ __ ___   ___ _ __ 
    | | | | / __|/ __| |/ _` | | '_ ` _ \ / _ \ '__|
    | |_| | \__ \ (__| | (_| | | | | | | |  __/ |   
    |____/|_|___/\___|_|\__,_|_|_| |_| |_|\___|_|

    
    I recomend you leave the main.py and folderscanner.bat in a folder before running it.
    The script will create a file called 'dump.txt' in that direcotry and it will contain all the files you wanted to find. 
    THIS CODE CAN STILL BE BUGGY. REPORT ANYTHING IN THE GITHUB OR EDIT IT YOURSELF
    
    ''')
    ok = input("Press 1 to continue: ")

    if ok == '1':
        main()


def main():
    os.system('cls')
    print('''
     _____ ___  _     ____  _____ ____     ____   ____    _    _   _ 
    |  ___/ _ \| |   |  _ \| ____|  _ \   / ___| / ___|  / \  | \ | |
    | |_ | | | | |   | | | |  _| | |_) |  \___ \| |     / _ \ |  \| |
    |  _|| |_| | |___| |_| | |___|  _ <    ___) | |___ / ___ \| |\  |
    |_|   \___/|_____|____/|_____|_| \_\  |____/ \____/_/   \_\_| \_| v2.0
        

    ''')

    global directory

    directory = input("Input directory path: ").strip()
    while not Path(directory).is_dir():
        print("Invalid directory path. Try again.")
        directory = input("Input directory path: ").strip()
    main2()

def main2():
    os.system('cls')
    print(''' 
    Select a option:
        
    1. Specific FILE TYPE search
    2. Specific FILE NAME search
          


    ''')
    
    global filetype, filename

    choice = input("Select an option: ")

    if choice == '1':
        filetype = input("What is the file type?: ")

        if not filetype.startswith('.'):
            filetype = '.' + filetype
        filetypescan()
    
    elif choice == '2':
        filename = input("What is the file name(s)?: ")

        while not '.' in filename:
            print("Please provide a file type")
            filename = input("What is the file name(s)?: ")
        filenamescan()
    
def filetypescan():
    os.system('cls')
    folder_path = Path(directory)
    output_file = Path('dump.txt')

    matches = list(folder_path.rglob(f'*{filetype}'))

    if not matches:
        print(f"No files found with type '{filetype}'. No dump file created.")
        main2()

    with output_file.open('w', encoding='utf-8') as f:
        for entry in folder_path.rglob(f'*{filetype}'):
            if entry.is_file():
                print(f"Writing: {entry.resolve()}")
                f.write(str(entry.resolve()) + '\n')
    
    print(f"Dump created with {len(matches)} file(s) found.")

    choice = input("Copy files to a new folder for easier access? (Y/N): ").lower()

    if choice == "y":
        dest_folder = Path(input("Enter destination folder to copy the files to: ").strip())
        
    if not dest_folder.exists():
        create = input(f"Folder '{dest_folder}' does not exist. Create it? (Y/N): ").strip().lower()
        if create == 'y':
            dest_folder.mkdir(parents=True)
        else:
            print("Aborting copy.")
            return

    extract(matches, dest_folder)   
    
def filenamescan():
    os.system('cls')
    folder_path = Path(directory)
    output_file = Path('dump.txt')

    matches = list(folder_path.rglob(f'*{filename}'))

    if not matches:
        print(f"No files found with name '{filename}'. No dump file created.")
        main2()

    with output_file.open('w', encoding='utf-8') as f:
        for entry in folder_path.rglob(f'*{filename}'):
            if entry.is_file():
                print(f"Writing: {entry.resolve()}")
                f.write(str(entry.resolve()) + '\n')
    
    print(f"Dump created with {len(matches)} file(s) found.")

    choice = input("Copy files to a new folder for easier access? (Y/N): ").lower()

    if choice == "y":
        dest_folder = Path(input("Enter destination folder to copy the files to: ").strip())
        
    if not dest_folder.exists():
        create = input(f"Folder '{dest_folder}' does not exist. Create it? (Y/N): ").strip().lower()
        if create == 'y':
            dest_folder.mkdir(parents=True)
        else:
            print("Aborting copy.")
            return

    extract(matches, dest_folder)

def extract(matches, dest_root):
    os.system('cls')
    print("Saving files.")

    dest_root = Path(dest_root)
    if not dest_root.exists():
        dest_root.mkdir(parents=True)

    for file_path in matches:
        if file_path.is_file():
            safe_name = str(file_path.relative_to(directory)).replace(os.sep, '_').replace(':', '').replace(' ', '_')
            folder_name = dest_root / safe_name.rsplit('.', 1)[0]
            folder_name.mkdir(parents=True, exist_ok=True)

            destination_path = folder_name / file_path.name
            shutil.copy2(file_path, destination_path)
            print(f"Copied: {file_path} -> {destination_path}")


#Initial
disclaimer()

# POSSIBLE TO DO

# Scan all file types and ask which file extension you want?
# Recreate the directory of the specific file location in a different folder?