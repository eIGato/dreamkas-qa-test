#!.venv/bin/python
#vim :set filencoding=utf-8:

import requests
import json


host = 'http://localhost:8001'

# TODO: Use fixtures

def test_get_all_users_expect_status_200():
    response = requests.get(host+'/users')
    assert response.status_code == 200