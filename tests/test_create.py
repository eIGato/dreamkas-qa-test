#!.venv/bin/python
#vim :set filencoding=utf-8:

import requests
import json


host = 'http://localhost:8001'

# TODO: Delete test users after assertion

def test_create_without_company_expect_status_201():
    raw_data = {'username': 'John Doe',
                'email': 'j@hn.oe',
                'password': 'qwerty123'}
    response = requests.post(host+'/users', data=json.dumps(raw_data))
    assert response.status_code == 201

def test_create_without_email_expect_status_400():
    raw_data = {'username': 'John Doe',
                'password': 'qwerty123',
                'company': 'ExCorp'}
    response = requests.post(host+'/users', data=json.dumps(raw_data))
    assert response.status_code == 400