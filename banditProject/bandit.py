import json
from pwn import *

for i in range(1):
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

    session = ssh(username, address, password=password, port = port)

    sh = session.shell('/bin/sh')
    sh.sendline(command)

    password = sh.recvline().rstrip()

    with open('password.txt','wb') as f:
        f.write(password)
