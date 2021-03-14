# Finds txt files in cwd and copies them into a new folder.

import os, shutil
from pathlib import Path

for folderName, subfolders, filenames in os.walk('.'):
    for filename in filenames:
        if '.txt' in filename:
            shutil.copy(os.path.join(folderName,filename),Path.cwd()/'new_folder')














