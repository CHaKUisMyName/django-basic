from django.urls import path
from chakuapp import views

urlpatterns = [
    path('',views.index, name='chakuapp-index'),
    path('about',views.about),
    path('form',views.form),
    path('edit/<person_id>',views.edit),
    path('delete/<person_id>',views.delete),
]