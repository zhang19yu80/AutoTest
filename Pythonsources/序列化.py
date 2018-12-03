import json

dict1 = {
    'name': 'ZhangYu',
    'age': 38,
    'job': 'International'

}


f = open('test','w')

f.write(json.dumps(dict1))

f.close()