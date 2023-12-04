from django.urls import path
from .views import (
    budget_list,
    budget_detail,
    create_project,
    editProject,
    rate_table,
    project_update,
    project_delete,
    create_bom,
    bom,
    bom_update,
    create_service,
    service_update,
    bomSave,
    bom_edit,
)
from .import views

app_name="budgetTool"

urlpatterns = [
    path('', budget_list),
    path('<int:pk>',budget_detail),
    path('<int:pk>/update',project_update),
    path('<int:pk>/delete',project_delete),
    path('create/',create_project),
    path('rate_table/',rate_table),
    # path('<int:pk>/createservice/',create_service),
    # path('<int:fk>/<int:pk>/bom/',bom_update),
    path('<int:fk>/service/<int:pk>/',service_update),
    path('<int:pk>/bomSave/',bomSave),
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
    
    

    # path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),
    # path('rateTable',views.rate_table,name='rate_table')
]
