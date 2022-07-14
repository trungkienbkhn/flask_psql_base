import os
import requests


def test_api(variables):
    r = requests.get(os.path.join(variables['url'], "api/status"))
    assert r.status_code == 200
    r = requests.post(os.path.join(variables['url'], "api/status"))
    assert r.status_code == 405
