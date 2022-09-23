import json

with open('File.json') as File:
    data = json.load(File)

    for item in data['Student_data']:
        print(item)
        print(item.keys())
        print(item.values())









