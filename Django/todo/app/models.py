from django.db import models

# Create your models here.
class Details(models.Model):
    task_name = models.CharField(max_length=255,unique=True)
    task_desc = models.CharField(max_length=200)
    task_status = models.BooleanField(default=False)