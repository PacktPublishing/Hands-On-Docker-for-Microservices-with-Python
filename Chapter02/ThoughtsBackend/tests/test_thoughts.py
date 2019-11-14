'''
Test the Thoughts operations


Use the thought_fixture to have data to retrieve, it generates three thoughts
'''
from unittest.mock import ANY
import http.client
from freezegun import freeze_time
from .constants import PRIVATE_KEY
from thoughts_backend import token_validation
from faker import Faker
fake = Faker()


@freeze_time('2019-05-07 13:47:34')
def test_create_me_thought(client):
    new_thought = {
        'username': fake.name(),
        'text': fake.text(240),
    }
    header = token_validation.generate_token_header(fake.name(),
                                                    PRIVATE_KEY)
    headers = {
        'Authorization': header,
    }
    response = client.post('/api/me/thoughts/', data=new_thought,
                           headers=headers)
    result = response.json

    assert http.client.CREATED == response.status_code

    expected = {
        'id': ANY,
        'username': ANY,
        'text': new_thought['text'],
        'timestamp': '2019-05-07T13:47:34',
    }
    assert result == expected


def test_create_me_unauthorized(client):
    new_thought = {
        'username': fake.name(),
        'text': fake.text(240),
    }
    response = client.post('/api/me/thoughts/', data=new_thought)
    assert http.client.UNAUTHORIZED == response.status_code


def test_list_me_thoughts(client, thought_fixture):
    username = fake.name()
    text = fake.text(240)

    # Create a new thought
    new_thought = {
        'text': text,
    }
    header = token_validation.generate_token_header(username,
                                                    PRIVATE_KEY)
    headers = {
        'Authorization': header,
    }
    response = client.post('/api/me/thoughts/', data=new_thought,
                           headers=headers)
    result = response.json

    assert http.client.CREATED == response.status_code

    # Get the thoughts of the user
    response = client.get('/api/me/thoughts/', headers=headers)
    results = response.json

    assert http.client.OK == response.status_code
    assert len(results) == 1
    result = results[0]
    expected_result = {
        'id': ANY,
        'username': username,
        'text': text,
        'timestamp': ANY,
    }
    assert result == expected_result


def test_list_me_unauthorized(client):
    response = client.get('/api/me/thoughts/')
    assert http.client.UNAUTHORIZED == response.status_code


def test_list_thoughts(client, thought_fixture):
    response = client.get('/api/thoughts/')
    result = response.json

    assert http.client.OK == response.status_code
    assert len(result) > 0

    # Check that the ids are increasing
    previous_id = -1
    for thought in result:
        expected = {
            'text': ANY,
            'username': ANY,
            'id': ANY,
            'timestamp': ANY,
        }
        assert expected == thought
        assert thought['id'] > previous_id
        previous_id = thought['id']


def test_list_thoughts_search(client, thought_fixture):
    username = fake.name()
    new_thought = {
        'username': username,
        'text': 'A tale about a Platypus'
    }
    header = token_validation.generate_token_header(username,
                                                    PRIVATE_KEY)
    headers = {
        'Authorization': header,
    }
    response = client.post('/api/me/thoughts/', data=new_thought,
                           headers=headers)
    assert http.client.CREATED == response.status_code

    response = client.get('/api/thoughts/?search=platypus')
    result = response.json

    assert http.client.OK == response.status_code
    assert len(result) > 0

    # Check that the returned values contain "platypus"
    for thought in result:
        expected = {
            'text': ANY,
            'username': username,
            'id': ANY,
            'timestamp': ANY,
        }
        assert expected == thought
        assert 'platypus' in thought['text'].lower()


def test_get_thought(client, thought_fixture):
    thought_id = thought_fixture[0]
    response = client.get(f'/api/thoughts/{thought_id}/')
    result = response.json

    assert http.client.OK == response.status_code
    assert 'text' in result
    assert 'username' in result
    assert 'timestamp' in result
    assert 'id' in result


def test_get_non_existing_thought(client, thought_fixture):
    thought_id = 123456
    response = client.get(f'/api/thoughts/{thought_id}/')

    assert http.client.NOT_FOUND == response.status_code
