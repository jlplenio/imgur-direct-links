import logging
import os

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class Database:

    def __init__(self):
        self.database_url = os.environ['DATABASE_URL']
        self.connection = psycopg2.connect(self.database_url, sslmode='require')
        self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        self.cursor = self.connection.cursor()

    def query(self, query):
        self.cursor.execute(query)
        try:
            return self.cursor.fetchall()
        except:
            return None

    def __del__(self):
        self.connection.close()


class Dao:

    def __init__(self):
        self.database = Database()

    def get_counter(self, name):
        logging.debug(f"counter {name} requested")
        return self.database.query("SELECT {} from counters WHERE id=1".format(name))

    def inc_counter(self, name):
        logging.debug(f"counter {name} incremented")
        return self.database.query("UPDATE counters SET {0} = {0} + 1 WHERE id=1".format(name))