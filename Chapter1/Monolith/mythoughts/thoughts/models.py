from django.db import models


class UserModel(models.Model):
    username = models.CharField(max_length=50)
    password_hash = models.CharField(max_length=100)


class SessionModel(models.Model):
    session = models.CharField(max_length=50)


class ThoughModel(models.Model):
    user = models.CharField(max_length=50)
    text = models.CharField(max_length=250)
