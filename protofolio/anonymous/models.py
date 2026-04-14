from django.db import models

# Create your models here.
class contact_master(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    message = models.CharField(max_length=200)
    remark = models.CharField(max_length=200)