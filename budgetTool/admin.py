from django.contrib import admin
from .models import RateTable,User,Project,Service,Sales,BillOfMaterials,ServiceCategory,BOMCategory

admin.site.register(RateTable)
admin.site.register(User)
admin.site.register(Project)
admin.site.register(Service)
admin.site.register(Sales)
admin.site.register(BillOfMaterials)
admin.site.register(ServiceCategory)
admin.site.register(BOMCategory)

