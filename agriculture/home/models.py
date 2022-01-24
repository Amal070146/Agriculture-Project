from django.db import models

# Create your models here.

class User(models.Model):
    uid = models.AutoField(primary_key=True)
    cs_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    adr = models.CharField(max_length=80)
    email = models.CharField(max_length=40)
    mobile = models.CharField(max_length=10)
    gender = models.CharField(max_length=6)
    age = models.CharField(max_length=3)
    occupation = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.first_name} {self.last_name} -> {self.occupation}"
    
class Cold_storage(models.Model):
    cs_own = models.ForeignKey(User,on_delete=models.CASCADE)
    cs_pname = models.CharField(max_length=40)
    cs_max_str = models.IntegerField()
    cs_avl_str = models.IntegerField()
    def __str__(self):
        return f"{self.cs_own.first_name} {self.cs_own.last_name} -> \t\t{self.cs_pname}\t\tMax:{self.cs_max_str}"
