import os

# Set the directory containing the files and folders you want to modify
directory = '/run/media/arpit/DATA/Downloads/Music/08 - Voice Drama/New Folder/'

# Set the character to replace and the replacement character


def translate_names(dir, old_char, new_char):
    # Iterate through the files and folders in the directory
    for filename in os.listdir(dir):
        # Use translate-shell to translate the file or folder name
        new_name = filename.replace(old_char, new_char)
        os.rename(os.path.join(dir, filename), os.path.join(dir, new_name))

    # Recursively translate the names in any subdirectories
    for subdir in os.listdir(dir):
        if os.path.isdir(os.path.join(dir, subdir)):
            translate_names(os.path.join(dir, subdir), old_char, new_char)


# Start the recursive translation process
translate_names(directory, 'ｃｄ', 'CD')
translate_names(directory, '・', ' & ')
translate_names(directory, '_', '. ')

print('Finished replacing characters in names!')
