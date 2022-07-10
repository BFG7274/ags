import requests


def default_send_request(tags, title, text):
    # send

    try:
        response = requests.get(
            url="",
            params={
                "tag": tags,
                "title": title,
                "text": text,
                "mode": "html",
            },
        )
        if response.status_code/100 == 2:
            pass

    except requests.exceptions.RequestException:
        print(' Notify HTTP Request failed')