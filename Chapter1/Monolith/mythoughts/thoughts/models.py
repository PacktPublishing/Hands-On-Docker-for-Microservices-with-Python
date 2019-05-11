from django.db import models


class UserModel(models.Model):
    username = models.CharField(max_length=50)
    password_hash = models.CharField(max_length=100)


class SessionModel(models.Model):
    session = models.CharField(max_length=50)


class ThoughtModel(models.Model):
    username = models.CharField(max_length=50)
    text = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now_add=True)
