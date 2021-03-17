#! Python 3
# Prints all files that are over 100MB

import os

for root, folders, filenames in os.walk('/'):
    for filename in filenames:
        abspath = os.path.abspath(os.path.join(root,filename))
        if not os.path.exists(abspath):
            continue
        if os.path.getsize(abspath) > 100000000:
            print(abspath)

