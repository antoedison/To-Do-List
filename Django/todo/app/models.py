from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Details(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255,unique=True)
    task_desc = models.CharField(max_length=200)
    task_status = models.BooleanField(default=False)