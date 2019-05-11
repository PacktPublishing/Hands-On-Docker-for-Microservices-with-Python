import bcrypt
from django.db import models
import random
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class UserModel(models.Model):
    username = models.CharField(max_length=50)
    password_hash = models.CharField(max_length=100)

    class IncorrectPassword(Exception):
        pass

    def check_password(self, password):
        '''
        Check the stored password, if incorrect will raise IncorrecPassword
        '''
        to_check = password.encode()
        db_hash = self.password_hash.encode()
        if bcrypt.hashpw(to_check, db_hash) == db_hash:
            # Valid password
            return True

        raise self.IncorrectPassword

    def login_user(self, password):
        self.check_password(password)

        return SessionModel.new_session(self.username)


class SessionModel(models.Model):
    session = models.CharField(max_length=50)
    username = models.CharField(max_length=50)

    @classmethod
    def new_session(cls, username):
        '''
        Create a new session for the user, store it,
        and clean old ones.
        '''
        new_session = random.getrandbits(248)
        logger.error(new_session)
        new = cls(session=new_session, username=username)
        # Delete old sessions
        cls.objects.filter(username=username).delete()
        # Save the new session
        new.save()

        # Set the cookie with the session
        return new_session


class ThoughtModel(models.Model):
    username = models.CharField(max_length=50)
    text = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now_add=True)
