# Walks through a folder tree and searches for files with a .txt extension.
# Copies these files from their location into a new folder.

import os, shutil

os.mkdir('new_folder')

for folder, subfolders, filenames in os.walk('.'):

    for filename in filenames:
        if '.git' in filename:
            continue
        if '.txt' in filename:
            filepath = os.path.join(folder,filename)
            if os.path.exists('./new_folder/'+filename):
                continue
            shutil.copy(filepath,'./new_folder')
