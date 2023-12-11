from django.db import models
from django.contrib.auth.models import AbstractUser

#  py .\manage.py shell
# from budgetTool.models import BillOfMaterials
# BillOfMaterials.objects.all().values() 

class User(AbstractUser):
    pass

class ServiceCategory(models.Model):
    index=models.IntegerField()
    name=models.CharField(max_length=300)
    def __str__(self):
        return (f"{self.name}")
    class Meta:
        ordering = ['index']

class BOMCategory(models.Model):
    index=models.IntegerField()
    name=models.CharField(max_length=300)
    def __str__(self):
        return (f"{self.name}")
    class Meta:
        ordering = ['index']


class RateTable(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    type=models.CharField(max_length=100)
    list=models.FloatField()
    cost=models.FloatField()

    def __str__(self):
        return (f"{self.type} {self.list} {self.cost}")
    
class Project(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=100)
    quote_BOM=models.IntegerField()
    quote_Service=models.IntegerField()
    adjust_Service=models.FloatField()
    adjust_BOM=models.FloatField()
    travel_weekly=models.IntegerField()

    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return (f"{self.name}")

class BillOfMaterials(models.Model):

    order = models.IntegerField(blank=True, default=1000)
    index=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=100)
    estimate_cost=models.IntegerField()
    sales_price=models.IntegerField()
    quantity=models.IntegerField()
    supplier=models.CharField(max_length=300,blank=True)
    actual_cost=models.FloatField()
    Responsible=models.CharField(max_length=300,blank=True)
    description=models.CharField(max_length=300,blank=True)
    notes=models.CharField(max_length=300,blank=True)
    
    bom_category=models.ForeignKey(BOMCategory,on_delete=models.SET_NULL, null=True,related_name='project_BOM_category')
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name='project_bom')

    def __str__(self):
        return (f"{self.name}")
    
    class Meta:
        ordering = ['order']


class Service(models.Model):

    SERVICE_TYPES = [
        ("Project Management", "Project Management"),
        ("Engineering (In House)", "Engineering (In House)"),
        ("Engineering (On Site)", "Engineering (On Site)"),
        ("Programming (In House)", "Programming (In House)"),
        ("Programming (On Site)", "Programming (On Site)"),
        ("Shipping/Procurement", "Shipping/Procurement"),
        ("Admin", "Admin"),
    ]

    # category=models.CharField(max_length=100,choices=SERVICE_CATEGORY)
    order = models.IntegerField(blank=True, default=1000)
    index=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=100,choices=SERVICE_TYPES)
    hours_estimated=models.IntegerField()
    hours_worked=models.IntegerField()
    
    rate_list=models.FloatField(default=0)
    rate_cost=models.FloatField(default=0)
    travel_actual=models.IntegerField()
    notes=models.CharField(max_length=300,blank=True)
    isOnSite=models.BooleanField(default=False)

    #calculated field
    hours_adjusted=models.FloatField(default=0)
    travel_estimate=models.FloatField(default=0)
    sub_total_list=models.IntegerField(default=0)
    sub_total_adjusted_list=models.IntegerField(default=0)
    sub_total_cost_est=models.IntegerField(default=0)
    sub_total_adjusted_cost_est=models.IntegerField(default=0)
    cost_actual=models.IntegerField(default=0)

    category=models.ForeignKey(ServiceCategory,on_delete=models.SET_NULL, null=True,related_name='project_service_category')
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name='project_service')
    def __str__(self):
        return (f"{self.name}--- {self.category}")
    
    class Meta:
        ordering = ['order']


class Sales(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class BoM(models.Model):
    name=models.CharField(max_length=100)
    total_bom_cost=models.IntegerField()

    def __str__(self):
        return (f"{self.name}")







    
