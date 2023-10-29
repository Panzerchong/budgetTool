from django.db import models

class RateTable(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    type=models.CharField(max_length=100)
    list=models.IntegerField()
    cost=models.IntegerField()

def __str__(self):
    return (f"{self.type} {self.list} {self.cost}")
    
