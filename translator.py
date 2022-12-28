
# Set the directory containing the files and folders you want to translate
import subprocess
import os
directory = '/run/media/arpit/DATA/OSTs/Visual Novels/07th Expansion/06 - Other & Crossovers/[2022.10.15] [MGPG-0001] Thanks／you -Sotsugyou- - M.Graveyard/New Folder'


# Set the source and target languages
source_language = 'ja'
target_language = 'en'

# Translate the names of files and folders in the specified directory and its subdirectories
confirmation = True
import re

def has_japanese_characters(s):
    pattern = r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]'
    return bool(re.search(pattern, s))

def translate_names(dir):
    # Iterate through the files and folders in the directory
    for filename in os.listdir(dir):
        # Use translate-shell to translate the file or folder name
        if(not has_japanese_characters(filename)):
            print(f'Skipped {filename}')
            continue
        oldName = filename
        translated_name = subprocess.run(
            ['trans', '-b', '-no-warn'
                f':{target_language}', oldName],
            capture_output=True,
            text=True
        ).stdout.strip()

        if confirmation:
            print(f'Change {oldName} to {translated_name}?(y/n)')
            resp = input()
            if resp != 'y' and resp != 'Y':
                continue

        # Rename the file or folder with the translated name
        os.rename(os.path.join(dir, filename),
                  os.path.join(dir, translated_name))
        print(f'Translated {oldName} To {translated_name}')

    # Recursively translate the names in any subdirectories
    for subdir in os.listdir(dir):
        if os.path.isdir(os.path.join(dir, subdir)):
            translate_names(os.path.join(dir, subdir))


# Start the recursive translation process
translate_names(directory)

print('Finished translating names!')
