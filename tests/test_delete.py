#!.venv/bin/python
#vim :set filencoding=utf-8:

import requests
import json


host = 'http://localhost:8001'

# TODO: Use fixtures

def test_delete_existing_user_expect_status_204():
    response = requests.delete(host+'/users/4')
    assert response.status_code == 204

def test_delete_nonexisting_user_expect_status_404():
    response = requests.delete(host+'/users/1000000')
    assert response.status_code == 404