from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=200)
    mail_address = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name