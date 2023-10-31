from django.urls import path
from .views import budget_list,budget_detail,create_project

app_name="budgetTool"

urlpatterns = [
    path('', budget_list),
    path('<int:pk>',budget_detail),
    path('create/',create_project)
    # path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),
    # path('rateTable',views.rate_table,name='rate_table')
]
