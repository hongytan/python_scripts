# Create a bunch of txt files with American date format

import random

for fileNum in range(20):
    month = random.randint(1,12)
    day = random.randint(1,31)
    year = random.randint(1900,2021)
    with open(f"file{fileNum+1}.{month}-{day}-{year}.txt",'w') as f:
        f.write(f"Hello! This is file{fileNum+1}. Goodbye.")
