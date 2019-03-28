import pickle
import os

from src import CONSTANTS


class Cacher:
    def __init__(self):
        self.dir_ = CONSTANTS.CACHE_FOLDER

        if not os.path.exists(self.dir_):
            os.mkdir(self.dir_)


    def add(self, data, email_address):
        filepath = self._create_file_path(email_address)

        if not os.path.exists(filepath):
            f = open(filepath, 'w')
            f.close()

        cache = self.load(email_address)

        with open(filepath, 'wb') as write:
            to_cache = cache + data
            pickle.dump(to_cache, write)

        return True


    def load(self, email_address):
        filepath = self._create_file_path(email_address)

        if not os.path.exists(filepath) or not os.path.getsize(filepath):
            return []

        with open(filepath, 'rb') as file_:
            data = pickle.load(file_)

        return data


    def delete_cache(self, email_address):
        filepath = self._create_file_path(email_address)

        if os.path.exists(filepath):
            os.remove(filepath)

        return True


    def _create_file_path(self, email_address):
        return os.path.join(self.dir_, email_address)

