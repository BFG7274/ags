import time
from pkg import db
from pkg.tmdbQuery import tmdbid_send_request


def nc_get_tmdbid(r, tmdbid):
    data = tmdbid_send_request(tmdbid)
    r['tmdbid'] = tmdbid
    r['name'] = data[0]
    r['year'] = data[1]
    r['season'] = data[2]
    return r


def nc_get(tmdbid):
    r = {}
    c = db.cs.execute(f"SELECT *  from nc_raws where tmdbid={tmdbid}")
    if len(list(c)) == 0:
        r = nc_get_tmdbid(r, tmdbid)
        r['createTime'] = int(round(time.time() * 1000))
        r['updateTime'] = r['createTime']
        r['level'] = 0
        nc_create(r)
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
            r = nc_get_tmdbid(r, tmdbid)
            r['updateTime'] = timeNow
            nc_update(r)
    return r


def nc_create(r):
    db.cs.execute(f"INSERT INTO nc_raws (tmdbid,name,year,level,createTime,updateTime,season) \
      VALUES ({r['tmdbid']}, {r['name']}, {r['year']}, {r['level']}, {r['createTime']},{r['updateTime']} ,{r['season']})")
    db.conn.commit()


def nc_level(tmdbid, level):
    db.cs.execute(
        f"UPDATE nc_raws set level = {level} where tmdbid={tmdbid}")
    db.conn.commit()


def nc_update(r):
    db.cs.execute(
        f"UPDATE nc_raws set updateTime = {r['updateTime']},season={r['season']} where tmdbid={r['tmdbid']}")
    db.conn.commit()
