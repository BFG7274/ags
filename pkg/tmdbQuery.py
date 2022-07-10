import logging
import sys
import requests
from config import conf


def tmdbid_send_request(tmdbid):
    # Request
    try:
        response = requests.get(
            url=f"https://api.themoviedb.org/3/tv/{tmdbid}",
            params={
                "api_key": conf['tmdb']['api_key'],
                "language": "en-US",
            },
        )
        if response.status_code > 299:
            logging.ERROR("TMDB does not work properly!")
            sys.exit(1)
        data = response.json()
        name = data['name']
        seasons = data['seasons']
        season = seasons[len(seasons)-1]['season_number']
        year = data['first_air_date'][:4]
        return name, year, season
    except requests.exceptions.RequestException:
        logging.ERROR('TMDB HTTP Request failed')
        sys.exit(1)
