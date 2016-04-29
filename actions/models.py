from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.


class Action(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    creation_date = models.DateField(default=date.today)
    user = models.ForeignKey(User)
