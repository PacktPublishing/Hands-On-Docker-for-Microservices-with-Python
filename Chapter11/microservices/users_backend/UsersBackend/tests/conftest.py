import pytest
from users_backend.app import create_app


@pytest.fixture
def app():
    application = create_app(script=True)

    application.app_context().push()
    # Initialise the DB
    application.db.create_all()

    return application
