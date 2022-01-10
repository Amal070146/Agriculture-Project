from django.db import models

# Create your models here.

class User(models.Model):
    uid = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    adr = models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    mobile = models.CharField(max_length=10)
    gender = models.CharField(max_length=6)
    age = models.CharField(max_length=3)
    occupation = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.first_name} {self.last_name} -> {self.occupation}"
    
class Cold_storage(models.Model):
    cid = models.AutoField(primary_key=True)
    cs_name=models.CharField(max_length=40)
    cs_adr=models.CharField(max_length=50)
    cs_email=models.CharField(max_length=40)
    cs_mobile=models.CharField(max_length=10)
    cs_password=models.CharField(max_length=20)
    cs_max_str=models.CharField(max_length=70)
    cs_avl_str=models.CharField(max_length=70)
    def __str__(self):
        return f"{self.cs_name}"