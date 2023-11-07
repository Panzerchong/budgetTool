from django.db import models
from django.contrib.auth.models import AbstractUser

#  py .\manage.py shell
# from budgetTool.models import BillOfMaterials
# BillOfMaterials.objects.all().values() 

class User(AbstractUser):
    pass

class RateTable(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    type=models.CharField(max_length=100)
    list=models.IntegerField()
    cost=models.IntegerField()

    def __str__(self):
        return (f"{self.type} {self.list} {self.cost}")
    

class BoM(models.Model):
    name=models.CharField(max_length=100)
    total_bom_cost=models.IntegerField()

    def __str__(self):
        return (f"{self.name}")
    
class Project(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=100)
    quote=models.IntegerField()
    # bom=models.ForeignKey("BoM",on_delete=models.CASCADE)
    # service=models.ForeignKey("Service",on_delete=models.CASCADE)
    
    def __str__(self):
        return (f"{self.name}")

class BillOfMaterials(models.Model):
    BOM_CATEGORY = [
        ("CUSTOM HARDWARE", "Custom Hardware"),
        ("UMA SOLUTION", "UMA Solution"),
        ("CONTROLS", "Controls"),
        ("SOFTWARE", "Software"),
        ("PROTECTION PLANS", "Protection Plans"),
    ]

    category=models.CharField(max_length=100,choices=BOM_CATEGORY)
    index=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=100)
    
    quantity=models.IntegerField()
    supplier=models.CharField(max_length=300,blank=True)
    actual_cost=models.IntegerField()
    Responsible=models.CharField(max_length=300,blank=True)
    description=models.CharField(max_length=300,blank=True)
    Notes=models.CharField(max_length=300,blank=True)
    quote_one=models.IntegerField(null=True,blank=True)
    vender_one=models.CharField(max_length=200,blank=True)
    quote_two=models.IntegerField(null=True,blank=True)
    vender_two=models.CharField(max_length=200,blank=True)
    quote_three=models.IntegerField(null=True,blank=True)
    vender_three=models.CharField(max_length=200,blank=True)
    
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name='project_bom')

    def __str__(self):
        return (f"{self.name}")


class Service(models.Model):
    SERVICE_CATEGORY = [
        ("GENERAL PROJECT", "GENERAL PROJECT"),
        ("HARDWARE DEVELOPMENT", "HARDWARE DEVELOPMENT"),
        ("SOFTWARE DEVELOPMENT", "SOFTWARE DEVELOPMENT"),
        ("IMPLEMENTATION ", "IMPLEMENTATION "),
        ("FACTORY ACCEPTANCE TEST", "FACTORY ACCEPTANCE TEST"),
        ("SHIPPING", "SHIPPING"),
        ("INSTALLATION", "INSTALLATION"),
        ("SITE ACCEPTANCE TEST", "SITE ACCEPTANCE TEST"),
        ("TRAINING", "TRAINING"),
    ]

    SERVICE_TYPES = [
        ("Project Management", "Project Management"),
        ("Engineering (In House)", "Engineering (In House)"),
        ("Engineering (On Site)", "Engineering (On Site)"),
        ("Programming (In House)", "Programming (In House)"),
        ("Programming (On Site)", "Programming (On Site)"),
        ("Shipping/Procurement", "Shipping/Procurement"),
        ("Admin", "Admin"),
    ]

    name=models.CharField(max_length=100)
    category=models.CharField(max_length=100,choices=SERVICE_CATEGORY,default="GENERAL PROJECT")
    type=models.CharField(max_length=100,choices=SERVICE_TYPES,default="Admin")
    hours_estimated=models.IntegerField()
    hours_worked=models.IntegerField()
    travel_actual=models.IntegerField()

    total_service_cost=models.IntegerField()
    
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name='project_service')
    def __str__(self):
        return (f"{self.name}")


class Sales(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class CustomHardware(models.Model):
    name=models.CharField(max_length=100)
    quantity=models.IntegerField()
    actual_cost=models.IntegerField(null=True)
    bom=models.ForeignKey(BoM,on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.name}")





    
