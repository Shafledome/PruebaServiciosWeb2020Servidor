import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utilities.db as db


class Geocache:

    def __init__(self, geo_id: int = None, lat: float = None, lon: float = None, image: str = None, hint: str = None):
        self.id = geo_id
        self.lat = lat
        self.lon = lon
        self.image = image
        self.hint = hint

    @staticmethod
    def get_geocache(user_id: int):
        result = db.get(f'geocaches/{user_id}')
        return result

    @staticmethod
    def get_all_geocaches():
        return db.get('geocaches')

    @staticmethod
    def search_by_id(geo_id: str):
        result = db.get_by_key('geocaches', geo_id)
        # returns geocache values
        # if not found, returns None
        return result

    @staticmethod
    def create_geocache(geo_id: int, lat: float, lon: float, image: str, hint: str):
        data = {'lat': lat, 'lon': lon, 'image': image, 'hint': hint}
        db.create('geocaches', geo_id, data)

    @staticmethod
    def delete_geocache(geo_id: int):
        db.delete('geocaches', geo_id)

    @staticmethod
    def update_geo_value(geo_id: int, value_entry: str, value: str):
        data = {f'{value_entry}': value}
        db.update('geocaches', geo_id, data)

    @staticmethod
    def geocache_by_hint(hint: str):
        geocaches = db.get('geocaches')
        result = {}
        for geocache in geocaches:
            if hint in geocache[0].hint:
                result[geocache[0].id] = geocache
