import datetime
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utilities.db as db


class Logbook:

    def __init__(self, log_id: int = None, email: str = None, geocache: int = None, stamp: datetime = None):
        self.id = log_id
        self.email = email
        self.geocache = geocache
        self.stamp = stamp

    @staticmethod
    def get_logbook(log_id: str):
        result = db.get(f'logbooks/{log_id}')
        return result

    @staticmethod
    def get_all_logbooks():
        return db.get('logbooks')

    @staticmethod
    def search_by_id(log_id: str):
        result = db.get_by_key('logbooks', log_id)
        # returns logbooks values
        # if not found, returns None
        return result

    @staticmethod
    def create_logbook(log_id: int, email: str, geocache: int, stamp: datetime):
        data = {'id': log_id, 'email': email, 'geocache': geocache, 'stamp': stamp}
        db.create('logbooks', log_id, data)

    @staticmethod
    def delete_logbook(log_id: int):
        db.delete('logbooks', log_id)

    @staticmethod
    def update_log_value(log_id: int, value_entry: str, value: str):
        data = {f'{value_entry}': value}
        db.update('logbooks', log_id, data)

    @staticmethod
    def logbook_by_email(email: str):
        return db.get('logbooks', 'email', email)

    @staticmethod
    def geocache_not_found():
        geocaches = db.get('geocaches')
        logbooks = db.get('logbooks')
        filtered = filter()

    @staticmethod
    def filter_function(geocache, logbooks):
        result = True
        for logbook in logbooks:
            if geocache.keys()[0] == logbook[0].geocache:
                result = False
        return result
