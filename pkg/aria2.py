import json
import time
import requests


def send_aria2(conf, url, id):
    jsonreq = json.dumps({"jsonrpc": "2.0", "method": "aria2.addUri", "id": f"{time.time_ns()}", "params": [
                         f"token:{conf['aria2_secret']}",
                         [f"magnet:?xt=urn:btih:{url}"], {"dir": f"/mnt/extra/aria2/anime/{id}"}]})
    response = requests.post(f"{conf['aria2_url']}/jsonrpc", data=jsonreq)
