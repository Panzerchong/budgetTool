from django.urls import path
from .views import budget_list,budget_detail,create_project,rate_table,project_update,project_delete,create_bom,bom,bom_update,create_service,service_update

app_name="budgetTool"

urlpatterns = [
    path('', budget_list),
    path('<int:pk>',budget_detail),
    path('<int:pk>/update',project_update),
    path('<int:pk>/delete',project_delete),
    path('create/',create_project),
    path('rate_table/',rate_table),
    path('<int:pk>/createbom/',create_bom),
    path('<int:pk>/createservice/',create_service),
    path('<int:fk>/<int:pk>/bom/',bom_update),
    path('<int:fk>/service/<int:pk>/',service_update),

    # path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),
    # path('rateTable',views.rate_table,name='rate_table')
]
