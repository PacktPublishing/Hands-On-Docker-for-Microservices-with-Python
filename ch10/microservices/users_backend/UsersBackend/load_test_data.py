from users_backend.app import create_app
from users_backend.models import UserModel


if __name__ == '__main__':
    application = create_app()
    application.app_context().push()

    # Create some test data
    test_data = [
        # username, timestamp, text
        ('bruce', "bruce", "1962-05-01 00:00:00Z"),
        ('stephen', "stephen", "1963-06-01 00:00:00Z"),
    ]
    for username, password, creation in test_data:
        user = UserModel(username=username, password=password,
                         creation=creation)
        application.db.session.add(user)

    application.db.session.commit()
