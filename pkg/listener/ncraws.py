import logging
import time
import re
import json
from telethon import events
from config import conf
from db import db


def get_level(msg):
    if 'Baha' in msg:
        return 1
    if 'B-Global' in msg & '中文' in msg:
        return 2
    return 0


def get_tmdbid(msg):
    tmdbid_match = re.findall(
        r'https:\/\/www\.themoviedb\.org\/tv\/(\d*)(\-(.*))?', msg, re.I)
    print(len(tmdbid_match))
    return tmdbid_match[0]


def get_ep(msg):
    ep_match = re.findall(
        r'EP (\d*)', msg, re.I)
    print(len(ep_match))
    return ep_match


def nc_raws_listen(client, channel):
    @client.on(events.NewMessage(chats=conf['channel']['nc_raws']))
    async def newMessageListener(event):
        newMessage = event.message.message
        if 'magnet:?xt=urn:btih:' in newMessage:
            magnetMatch = re.findall(
                r'magnet:\?xt=urn:btih:([^\n\r\s]*)', newMessage, re.I)
            magnetUrl = f"magnet:?xt=urn:btih:{magnetMatch[0]}"
            tmdbid = get_tmdbid(newMessage)
            ep = get_ep(newMessage)
            level = get_level(newMessage)
            if tmdbid != 0 & ep > 0:
                info = db.nc_get(tmdbid)
                if level > info['level']:
                    info['level'] = level
                    db.nc_level(tmdbid, level)
                if info['level'] == 0:
                    print("level is 0")
                elif info['level'] == -1:
                    print("level is -1")
                else:
                    print("level pass")
            else:
                pass
