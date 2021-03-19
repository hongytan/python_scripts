import json
from pwn import *

with open('bandit1.cfg', 'r') as f:
    data = json.load(f)

password = data['Password']
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
