import json

with open('data.json') as mon_fichier:
    data=json.load(mon_fichier)

print(list(filter(lambda x: x['Status'] == 'todo', data)))