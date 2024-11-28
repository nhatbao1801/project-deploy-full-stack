'''
Tests for jwt flask app.
'''
import os
import json
import pytest

import main

SECRET = 'TestSecret'
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MzQwMTM4MTUsIm5iZiI6MTczMjgwNDIxNSwiZW1haWwiOiJuaGF0YmFvMTgwMUBnbWFpbC5jb20ifQ.FhdbW3VEajM5su_DgzrrNPfRfgwddeMF_vGWpdS2o4M'
EMAIL = 'nhatbao1801@gmail.com'
PASSWORD = '1801'

@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client



def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'
    assert False

def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
    assert False
