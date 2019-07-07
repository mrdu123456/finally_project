from django.db import models

# Create your models here.
class User(models.Model):
    uname=models.CharField(max_length=128)
    phone=models.CharField(max_length=128)
    email=models.CharField(max_length=128)
    pwd=models.CharField(max_length=128)
    class Meta:
        db_table='t_user'
