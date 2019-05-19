import pytest
import http.client
from thoughts_backend.app import create_app
from .test_config import PRIVATE_KEY
from thoughts_backend import token_validation
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
            'text': fake.text(240),
        }
        header = token_validation.generate_token_header(fake.name(),
                                                        PRIVATE_KEY)
        headers = {
            'Authorization': header,
        }
        response = client.post('/api/thoughts/', data=thought,
                               headers=headers)
        assert http.client.CREATED == response.status_code
        result = response.json
        thought_ids.append(result['id'])

    yield thought_ids

    # Clean up thoughts
    for thought_id in thought_ids:
        url = f'/api/thought/{thought_id}'
        client.delete(url)
