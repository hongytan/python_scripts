# Walks through a folder tree and searches for files with a .txt extension.
# Copies these files from their location into a new folder.

import os, shutil

os.mkdir('new_folder')

for folder, subfolders, filenames in os.walk('.'):

    for filename in filenames:
        if '.txt' in os.path.join(folder,filename):
            print(shutil.copy(os.path.join(folder,filename),'./new_folder'))
            #shutil.copy(os.path.join(folder,filename),'./new_folder')


