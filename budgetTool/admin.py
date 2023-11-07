from django.contrib import admin
from .models import RateTable,User,Project,BoM,Service,Sales,CustomHardware,BillOfMaterials

admin.site.register(RateTable)
admin.site.register(User)
admin.site.register(Project)
admin.site.register(BoM)
admin.site.register(Service)
admin.site.register(Sales)
admin.site.register(CustomHardware)
admin.site.register(BillOfMaterials)

