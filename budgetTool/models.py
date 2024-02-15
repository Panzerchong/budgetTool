from django.db import models
from django.contrib.auth.models import User

#  py .\manage.py shell
# from budgetTool.models import BillOfMaterials
# BillOfMaterials.objects.all().values() 


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
    isTemplate=models.BooleanField(default=True)
    cost_est_bom=models.FloatField(default=0,blank=True)
    cost_est_service=models.FloatField(default=0,blank=True)
    cost_adjusted_bom=models.FloatField(default=0,blank=True)
    cost_adjusted_service=models.FloatField(default=0,blank=True)
    list_bom=models.FloatField(default=0,blank=True)
    list_service=models.FloatField(default=0,blank=True)
    list_adjusted_bom=models.FloatField(default=0,blank=True)
    list_adjusted_service=models.FloatField(default=0,blank=True)
    actual_bom=models.FloatField(default=0,blank=True)
    actual_service=models.FloatField(default=0,blank=True)
    hours=models.FloatField(default=0,blank=True)
    hours_adjusted=models.FloatField(default=0,blank=True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return (f"{self.name}")

class BillOfMaterials(models.Model):
    order = models.IntegerField(blank=True, default=1000)
    index=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=100)
    estimate_cost=models.IntegerField()
    sales_price=models.IntegerField(blank=True,null=True)
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

class RateTableCost(models.Model):
    order = models.IntegerField(blank=True, default=1000)
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=100)
    base=models.IntegerField()
    y1=models.IntegerField(null=True,blank=True)
    y2=models.IntegerField(null=True,blank=True)
    y3=models.IntegerField(null=True,blank=True)
    y4=models.IntegerField(null=True,blank=True)
    labor_cost=models.IntegerField(null=True,blank=True)
    labor_in_house=models.FloatField(default=165)
    labor_on_site=models.FloatField(default=287.5)
    employee=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return (f"{self.name}")
    
    class Meta:
        ordering = ['order']

class Service(models.Model):
    # category=models.CharField(max_length=100,choices=SERVICE_CATEGORY)
    order = models.IntegerField(blank=True, default=1000)
    index=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=100)
    hours_estimated=models.FloatField()
    hours_worked=models.FloatField(blank=True)
    rate_list=models.FloatField(blank=True,default=0)
    rate_cost=models.FloatField(blank=True,default=0)
    travel_actual=models.IntegerField(blank=True)
    notes=models.CharField(max_length=300,blank=True)
    isOnSite=models.BooleanField(default=False)
    #calculated field
    hours_adjusted=models.FloatField(default=0)
    travel_estimate=models.FloatField(default=0)
    sub_total_list=models.IntegerField(default=0)
    sub_total_adjusted_list=models.IntegerField(default=0)
    sub_total_cost_est=models.IntegerField(default=0)
    sub_total_adjusted_cost_est=models.IntegerField(default=0)
    cost_actual=models.FloatField(default=0)

    category=models.ForeignKey(ServiceCategory,on_delete=models.SET_NULL, null=True,related_name='project_service_category')
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name='project_service')
    type=models.ForeignKey(RateTableCost,on_delete=models.SET_NULL,null=True, related_name='project_service_type')
    def __str__(self):
        return (f"{self.name}--- {self.category}")
    class Meta:
        ordering = ['order']

class BoM(models.Model):
    name=models.CharField(max_length=100)
    total_bom_cost=models.IntegerField()

    def __str__(self):
        return (f"{self.name}")
    
class Employee(models.Model):
    name=models.CharField(max_length=100)
    level=models.ForeignKey(RateTableCost,on_delete=models.SET_NULL, null=True,related_name='employee_level')

    def __str__(self):
        return (f"{self.name}")

class Vendor(models.Model):
    index=models.IntegerField(default=100)
    name=models.CharField(max_length=100)
    def __str__(self):
        return (f"{self.name}")
    class Meta:
        ordering = ['index']

class Product_Price(models.Model):
    order = models.IntegerField(blank=True, default=1000)
    item=models.CharField(max_length=100)
    cost=models.FloatField()
    list=models.FloatField()
    margin=models.FloatField(null=True,blank=True)
    note=models.CharField(max_length=1000,null=True,blank=True)
    vendor=models.ForeignKey(Vendor,on_delete=models.SET_NULL, null=True,related_name='product_vendor')
    def __str__(self):
        return (f"{self.item}")
    class Meta:
        ordering = ['order']


class Summary(models.Model):
    cost_est=models.FloatField()
    cost_adjusted=models.FloatField()
    list=models.FloatField()
    list_adjusted=models.FloatField()
    actual=models.FloatField()
    list_margin=models.FloatField()
    list_adjusted_margin=models.FloatField()
    quoted_margin=models.FloatField()
    actual_margin=models.FloatField()

class Margins(models.Model):
    margin_est_bom=models.FloatField()
    margin_est_service=models.FloatField()
    margin_adjusted_bom=models.FloatField()
    margin_adjusted_service=models.FloatField()
    margin_actual_bom=models.FloatField()
    margin_actual_service=models.FloatField()
    margin_quoted_bom=models.FloatField()

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bom_index=models.JSONField(blank=True,null=True)
    service_index=models.JSONField(blank=True,null=True)
    RateTable_index=models.JSONField(blank=True,null=True)
    Product_Price_index=models.JSONField(blank=True,null=True)

    def __str__(self):
        return (f"{self.user}'s profile")
    
