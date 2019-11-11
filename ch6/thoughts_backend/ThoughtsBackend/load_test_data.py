from thoughts_backend.app import create_app
from thoughts_backend.models import ThoughtModel


if __name__ == '__main__':
    application = create_app()
    application.app_context().push()

    # Create some test data
    test_data = [
        # username, timestamp, text
        ('bruce', "1962-05-11 09:53:41Z",
         "A few seconds more and we'll know whether we have "
         "succeeded or not!"),
        ('bruce', "1962-05-11 09:58:23Z",
         "And now, if you'll excuse me, it's time for the final countdown"),
        ('bruce', "1962-05-11 10:07:13Z",
         "In a few seconds we will finally learn what happens when the "
         "powerful gamma rays are released"),
        ('stephen', "1963-06-11 19:53:41Z",
         "Naturally! All who come to me are! Speak..."),
        ('stephen', "1963-06-11 19:58:23Z",
         "Tonight I shall visit you! I shall find the answer to your dream! "
         "Now go"),
    ]
    for username, timestamp, text in test_data:
        thought = ThoughtModel(username=username, text=text,
                               timestamp=timestamp)
        application.db.session.add(thought)

    application.db.session.commit()
