import pyrebase
import os
import json
from dotenv import load_dotenv

load_dotenv()
config = json.loads(os.getenv('config'))

firebase = pyrebase.initialize_app(config)

db = firebase.database()


# users_by_score = db.child("users").order_by_child("score").equal_to(10).get()
# This query will return users with a score of 10
# users_by_name = db.child("users").order_by_child("name").get()
# This query will return users ordered by name
def get(entry, order=None, value=None):
    if value is not None and order is not None:
        result = db.child(entry).order_by_child(order).equal_to(value).get().val()
    elif order is not None:
        result = db.child(entry).order_by_child(order).get().val()
    else:
        result = db.child(entry).get().val()
    return result


def get_by_key(entry, key):
    return db.child(entry).child(key).get().val()


def create(entry, key, data):
    db.child(entry).child(key).set(data)


def update(entry, key, data):
    db.child(entry).child(key).update(data)


def delete(entry, key):
    db.child(entry).child(key).remove()


if __name__ == '__main__':
    with open('../script.json') as json_file:
        images = json.load(json_file)
        for element in images:
            new_image_data = {'id': element.id, 'lat': element.lat, 'lon': element.lon, 'url': element.url, 'hint': element.hint}
            create('images', element.id, new_image_data)
