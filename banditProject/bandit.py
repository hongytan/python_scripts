import json

with open('bandit1.cfg', 'r') as f:
    data = json.load(f)

for key in data:
    print(data[key])