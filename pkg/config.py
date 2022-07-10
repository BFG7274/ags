
from pkg.db import init as db_init


class config:
    def init(self):
        self.tmdb_api = "https://api.themoviedb.org/3"
        self.tmdb_key = "1234"
        self.telegram_api_id = ""
        self.telegram_api_hash = ""
        self.port = ""
        self.aria2_secret = ""
        self.aria2_url = ""

    def setDb(self, db):
        self.db = db


def init():
    conf = config()
    config.init()
    db = db_init(conf)
    conf.setDb(db)
    return conf
