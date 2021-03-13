# Opens all .txt files in cwd and searches for lines that match a user-supplied regex

from pathlib import Path
import re

regex = input('Enter a regex: ')

for textFile in list(Path.cwd().glob('*.txt')):
    with open(textFile,'r') as f:
        fContent = f.readlines()
        for line in fContent:
            x = re.search(regex,line)
            if (x):
                print('yay',line)
            else:
                print("nay",line)

