from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class RateTable(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    type=models.CharField(max_length=100)
    list=models.IntegerField()
    cost=models.IntegerField()

    def __str__(self):
        return (f"{self.type} {self.list} {self.cost}")
    
class Project(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=100)
    bom=models.ForeignKey("BoM",on_delete=models.CASCADE)
    service=models.ForeignKey("Service",on_delete=models.CASCADE)

class BoM(models.Model):
    total_bom_cost=models.IntegerField()

class Service(models.Model):
    total_service_cost=models.IntegerField()

class Sales(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)




    
