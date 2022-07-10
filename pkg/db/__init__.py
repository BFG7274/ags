import sqlite3
import time
from config import conf
from pkg.tmdbQuery import tmdbid_send_request


class dbInfo:
    def __init__(self):
        self.path = conf['db']
        self.conn = sqlite3.connect(self.path)
        self.cs = self.conn.cursor()

    def nc_get_tmdbid(self, r, tmdbid):
        data = tmdbid_send_request(tmdbid)
        r['tmdbid'] = tmdbid
        r['name'] = data[0]
        r['year'] = data[1]
        r['season'] = data[2]
        return r

    def nc_get(self, tmdbid):
        r = {}
        c = self.cs.execute(f"SELECT *  from nc_raws where tmdbid={tmdbid}")
        if len(list(c)) == 0:
            r = self.nc_get_tmdbid(r, tmdbid)
            r['createTime'] = int(round(time.time() * 1000))
            r['updateTime'] = r['createTime']
            r['level'] = 0
            self.nc_create(r)
        else:
            t = c.fetchone()
            r['tmdbid'] = t[1]
            r['name'] = t[2]
            r['year'] = t[3]
            r['level'] = t[4]
            r['createTime'] = t[5]
            r['updateTime'] = t[6]
            r['season'] = t[7]
            if r['level'] == 0 | r['level'] == -1:
                return r
            timeNow = int(round(time.time() * 1000))
            if timeNow-r['updateTime'] > 10000:
                self.nc_get_tmdbid(r, tmdbid)
                r['updateTime'] = timeNow
                self.nc_update(r)
        return r

    def nc_create(self, r):
        self.cs.execute(f"INSERT INTO nc_raws (tmdbid,name,year,level,createTime,updateTime,season) \
      VALUES ({r['tmdbid']}, {r['name']}, {r['year']}, {r['level']}, {r['createTime']},{r['updateTime']} ,{r['season']})")
        self.conn.commit()

    def nc_level(self, tmdbid, level):
        self.cs.execute(
            f"UPDATE nc_raws set level = {level} where tmdbid={tmdbid}")
        self.conn.commit()

    def nc_update(self, r):
        self.cs.execute(
            f"UPDATE nc_raws set updateTime = {r['updateTime']},season={r['season']} where tmdbid={r['tmdbid']}")
        self.conn.commit()


db = dbInfo()
