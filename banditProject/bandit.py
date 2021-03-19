import json
from pwn import *

for i in range(3):
    with open(f'bandit{i+1}.cfg', 'r') as f:
        data = json.load(f)
    try:
        password = data['Password']
    except:
        with open('password.txt','r') as fr:
            password = fr.read()
    port = data["Port"]
    username = data['Username']
    address = data['Address']
    command = data['Command']

    print(data)

    session = ssh(username, address, password=password, port = port)

    sh = session.shell('/bin/sh')
    sh.sendline(command)

    password = sh.recvline().rstrip().replace(b'$ ', b'')
    password = str(password).replace("b'",'').replace("'",'')

    with open('password.txt','w') as f:
        f.write(password)
