from django.urls import path
from .views import (
    budget_list,
    budget_detail,
    create_project,
    rate_table,
    project_delete,
)
from .import views

app_name="budgetTool"

urlpatterns = [
    path('', budget_list),
    path('<int:pk>',budget_detail),
    path('<int:pk>/delete',project_delete),
    path('create/',create_project),
    path('rate_table/',rate_table),
    
    # path('<int:pk>/update',project_update),
    # path('<int:pk>/createservice/',create_service),
    # path('<int:fk>/<int:pk>/bom/',bom_update),
    # path('<int:fk>/service/<int:pk>/',service_update),
    # path('<int:pk>/bomSave/',bomSave),
    #sytax for htmx
    path('<int:pk>/createBom',views.create_bom,name='create_bom'),
    path('edit/<int:pk>/',views.editProject,name='editProject'),
    path('<int:pk>/createService/',views.create_service,name='create_service'),
    path('<int:fk>/<int:pk>/bom/',views.bom_edit,name='bom_edit'),
    path('<int:pk>/bomDelete/',views.bom_delete,name='bom_delete'),
    path('<int:fk>/<int:pk>/service/',views.service_edit,name='service_edit'),
    path('<int:pk>/serviceDelete/',views.service_delete,name='service_delete'),
    path('<int:pk>/serviceOrder/',views.service_order,name='service_order'),
    path('<int:pk>/bomOrder/',views.bom_order,name='bom_order'),
    path('bomCategory/<int:pk>/',views.bom_category_edit,name='bom_category_edit'),
    path('createBomCategory/',views.create_bom_category,name='create_bom_category'),
    path('bomCategoryDelete/<int:pk>/',views.bom_category_delete,name='bom_category_delete'),
    path('serviceCategory/<int:pk>/',views.service_category_edit,name='service_category_edit'),
    path('createServiceCategory/',views.create_service_category,name='create_service_category'),
    path('download/<int:pk>/',views.download_excel,name='download_excel'),
    path('rateTableCost',views.create_rateTableCost,name='create_rateTableCost'),
    path('rateTableCost/edit/<int:pk>/',views.rateCost_edit,name='rateCost_edit'),
    path('rateTableCost/delete/<int:pk>/',views.rateCost_delete,name='rateCost_delete'),
    path('price_sheet',views.price_sheet,name='price_sheet'),
    path('create_product_price/<int:fk>',views.create_product_price,name='create_product_price'),
    path('product_price_edit/<int:pk>/<int:fk>',views.product_price_edit,name='product_price_edit'),
    path('product_price_delete/<int:pk>',views.product_price_delete,name='product_price_delete'),
    
    

    # path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),
    # path('rateTable',views.rate_table,name='rate_table')
]
