# Replaces substitute words with inputs from user in madlib.txt
from pathlib import Path

with open(Path.cwd() / 'file.txt','r') as f:
    fContent = f.read()
    fContentList = fContent.split()

    for word in fContentList:
        if word == "ADJECTIVE":
            userWord = input('Enter an adjective:\n')
            fContent = fContent.replace(word,userWord,1)

        elif word == word.upper():
            userWord = input(f'Enter a {word.lower()}:\n')
            fContent = fContent.replace(word,userWord,1)

print(fContent)

with open('newFile.txt','w') as f:
    f.write(fContent)

