from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    game_in_company = models.BooleanField(default=False)
    game_in_online = models.BooleanField(default=False)
