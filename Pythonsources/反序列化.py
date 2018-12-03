import json

f = open('test','r')
f1 = json.loads(f.read())
print(f1['age'])

