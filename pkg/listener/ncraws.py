from pkg.log import log
import time
import re
import json
from telethon import events
from config import conf
from db import db
from pkg import nc_get


def get_level(msg):
    if 'Baha' in msg:
        return 1
    if 'B-Global' in msg & '中文' in msg:
        return 2
    return 0


def get_tmdbid(msg):
    tmdbid_match = re.findall(
        r'https:\/\/www\.themoviedb\.org\/tv\/(\d*)(:\-(.*))?', msg, re.I)
    if len(tmdbid_match) >= 1:
        return tmdbid_match[1], True
    return -1, False


def get_ep(msg):
    ep_match = re.findall(
        r'EP (\d*)', msg, re.I)
    if len(ep_match) >= 1:
        return ep_match[1], True
    return -1, False


def get_url(msg):
    if 'magnet:?xt=urn:btih:' in msg:
        magnetMatch = re.findall(
            r'magnet:\?xt=urn:btih:([^\n\r\s]*)', msg, re.I)
        magnetUrl = f"magnet:?xt=urn:btih:{magnetMatch[0]}"
        return magnetUrl, True
    else:
        return "", False


def parse_nc_raws(msg):
    url, ok = get_url(msg)
    if not ok:
        log.DEBUG("Skipping because it does not have download links",
                  "nc_raws_listener")
        return
    tmdbid, ok = get_tmdbid(msg)
    if not ok:
        log.ERROR(f"Can not get tmdbid from\n{msg}", "nc_raws_listener")
        return
    ep, ok = get_ep(msg)
    if not ok:
        log.INFO(
            f"Skipping because can not get ep number\n{msg}", "nc_raws_listener")
        return
    level = get_level(msg)
    if level == 0:
        log.INFO(
            f"Skipping because it does not have chinese subs\n{msg}", "nc_raws_listener")
        return
    info = nc_get(tmdbid)
    if level > info['level']:
        info['level'] = level
        db.nc_level(tmdbid, level)
    if info['level'] == 0:
        print("level is 0")
    elif info['level'] == -1:
        print("level is -1")
    else:
        print("level pass")


def nc_raws_listen(client, channel):
    @client.on(events.NewMessage(chats=conf['channel']['nc_raws']))
    async def newMessageListener(event):
        newMessage = event.message.message
        parse_nc_raws(newMessage)
