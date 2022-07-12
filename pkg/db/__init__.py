import sqlite3
import time
from config import conf

class dbInfo:
    def __init__(self):
        self.path = conf['db']
        self.conn = sqlite3.connect(self.path)
        self.cs = self.conn.cursor()

db = dbInfo()
