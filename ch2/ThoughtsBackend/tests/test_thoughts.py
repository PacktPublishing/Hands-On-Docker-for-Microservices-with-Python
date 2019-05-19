'''
Test the Thoughts operations


Use the thought_fixture to have data to retrieve, it generates three thoughts
'''
from unittest.mock import ANY
import http.client
from freezegun import freeze_time
from faker import Faker
fake = Faker()


@freeze_time('2019-05-07 13:47:34')
def test_create_thought(client):
    new_thought = {
        'username': fake.name(),
        'text': fake.text(240),
    }
    response = client.post('/api/thoughts/', data=new_thought)
    result = response.json

    assert http.client.CREATED == response.status_code

    expected = {
        'id': ANY,
        'username': new_thought['username'],
        'text': new_thought['text'],
        'timestamp': '2019-05-07T13:47:34',
    }
    assert result == expected


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


def test_get_thought(client, thought_fixture):
    thought_id = thought_fixture[0]
    response = client.get(f'/api/thoughts/{thought_id}')
    result = response.json

    assert http.client.OK == response.status_code
    assert 'text' in result
    assert 'username' in result
    assert 'timestamp' in result
    assert 'id' in result


def test_get_non_existing_thought(client, thought_fixture):
    thought_id = 123456
    response = client.get(f'/api/thoughts/{thought_id}')

    assert http.client.NOT_FOUND == response.status_code
