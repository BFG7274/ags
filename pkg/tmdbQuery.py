

import requests


def tmdbid_send_request(conf, tmdbid):
    # Request

    try:
        response = requests.get(
            url=f"https://api.themoviedb.org/3/tv/{tmdbid}",
            params={
                "api_key": conf['tmdb_key'],
                "language": "en-US",
            },
        )
        data = response.json()
        name = data['name']
        seasons = data['seasons']
        season = seasons[len(seasons)-1]['season_number']
        year = data['first_air_date'][:4]
        return name, year, season
    except requests.exceptions.RequestException:
        print('tmdbid HTTP Request failed')


def test():
    conf = {
        'tmdb_key': ''
    }
    tmdbid = '67075'
    tmdbid_send_request(conf, tmdbid)


if __name__ == '__main__':
    test()
