from django.contrib import admin
from .models import RateTable,Project,Service,BillOfMaterials,ServiceCategory,BOMCategory,RateTableCost,Employee,Vendor,Product_Price,Profile

admin.site.register(RateTable)
admin.site.register(Project)
admin.site.register(Service)
admin.site.register(BillOfMaterials)
admin.site.register(ServiceCategory)
admin.site.register(BOMCategory)
admin.site.register(RateTableCost)
admin.site.register(Employee)
admin.site.register(Vendor)
admin.site.register(Product_Price)
admin.site.register(Profile)


