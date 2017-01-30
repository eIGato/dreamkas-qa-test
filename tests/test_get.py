#!.venv/bin/python
#vim :set filencoding=utf-8:

import requests
import json


host = 'http://localhost:8001'

# TODO: Use fixtures

def test_get_existing_user_expect_status_200():
    response = requests.get(host+'/users/1')
    assert response.status_code == 200

def test_get_nonexisting_user_expect_status_404():
    response = requests.get(host+'/users/1000000')
    assert response.status_code == 404