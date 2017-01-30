#!.venv/bin/python
#vim :set filencoding=utf-8:

import requests
import json


host = 'http://localhost:8001'

# TODO: Use fixtures to change a certain user

def test_change_password_to_good_expect_status_200():
    raw_data = {'password': 'qwerty1234'}
    response = requests.patch(host+'/users/10', data=json.dumps(raw_data))
    assert response.status_code == 200

def test_change_password_to_bad_expect_status_400():
    raw_data = {'password': 'q'}
    response = requests.patch(host+'/users/10', data=json.dumps(raw_data))
    assert response.status_code == 400