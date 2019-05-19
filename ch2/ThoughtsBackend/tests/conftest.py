import pytest
import http.client
from thoughts_backend.app import create_app
from faker import Faker
fake = Faker()


@pytest.fixture
def app():
    application = create_app()

    application.app_context().push()
    # Initialise the DB
    application.db.create_all()

    return application


@pytest.fixture
def thought_fixture(client):
    '''
    Generate three thoughts in the system.
    '''

    thought_ids = []
    for _ in range(3):
        thought = {
            'username': fake.name(),
            'text': fake.text(240),
        }
        response = client.post('/api/thoughts/', data=thought)
        assert http.client.CREATED == response.status_code
        result = response.json
        thought_ids.append(result['id'])

    yield thought_ids

    # Clean up thoughts
    for thought_id in thought_ids:
        url = f'/api/thought/{thought_id}'
        client.delete(url)
