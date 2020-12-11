import json
import pyrebase
import os
import json
from dotenv import load_dotenv

load_dotenv()
config = json.loads(os.getenv('config'))

firebase = pyrebase.initialize_app(config)

db = firebase.database()

'''
This file is used to load the given script.json file in firebase. script.json file was wrong, so it was changed.
'''


def create(entry, key, data):
    db.child(entry).child(key).set(data)


def add():
    with open('script.json') as json_file:
        images = json.load(json_file)
        for element in images:
            new_image_data = {'id': element['id'], 'lat': element['lat'], 'lon': element['lon'], 'url': element['url'], 'hint': element['hint']}
            create('geocaches', element['id'], new_image_data)


if __name__ == '__main__':
    add()
