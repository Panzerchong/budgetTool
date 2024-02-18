from django.urls import path
from django.contrib.auth.views import LoginView
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
    path('<int:fk>/<int:pk>/bom/copy',views.bom_copy,name='bom_copy'),
    path('<int:fk>/<int:pk>/bomDelete/',views.bom_delete,name='bom_delete'),
    path('<int:fk>/<int:pk>/service/',views.service_edit,name='service_edit'),
    path('<int:fk>/<int:pk>/service/copy',views.service_copy,name='service_copy'),
    path('<int:fk>/<int:pk>/serviceDelete/',views.service_delete,name='service_delete'),
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
    path('product_price_copy/<int:pk>/<int:fk>',views.product_price_copy,name='product_price_copy'),
    path('product_price_delete/<int:pk>',views.product_price_delete,name='product_price_delete'),
    path('costTableOrder/',views.rate_cost_order,name='rate_cost_order'),
    path('vendorForm/',views.create_vendor,name='create_vendor'),
    path('vendorForm/edit/<int:pk>/',views.vendor_edit,name='vendor_edit'),
    path('vendorForm/delete/<int:pk>/',views.vendor_delete,name='vendor_delete'),
    path('copyProject/<int:pk>',views.copy_project,name='copy_project'),
    path('priceSheetOrder/',views.price_sheet_order,name='price_sheet_order'),
    
    # path('', views.home, name='home'),
    path('register/', views.registerPage, name='registerPage'),
    path('changePassword/', views.change_password, name='change_password'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    # path('rateTable',views.rate_table,name='rate_table')
]

