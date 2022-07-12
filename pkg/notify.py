import logging
import sys
import requests
from pkg.config import conf
import aiohttp


async def default_send_request(tag, title, text):
    tags = ['ags']+tag
    try:
        response = requests.get(
            url=conf['zwarn']['url'],
            params={
                "tag": ','.join(tags),
                "title": title,
                "text": text,
                "mode": "html",
            },
        )
        if response.status_code > 299:
            logging.ERROR("Z-Warn does not work properly!")
            sys.exit(1)
    except requests.exceptions.RequestException:
        logging.ERROR(' Z-Warn HTTP Request failed')
        sys.exit(1)
