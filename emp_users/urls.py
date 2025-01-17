from django.urls import path
from emp_users import views

urlpatterns = [
    path('',views.index,name='emp-users-index'),
]