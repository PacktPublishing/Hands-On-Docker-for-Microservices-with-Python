from users_backend.app import create_app

if __name__ == '__main__':
    application = create_app()
    application.app_context().push()
    # Initialise the DB
    application.db.create_all()
