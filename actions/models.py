from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Action(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    creation_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User)
