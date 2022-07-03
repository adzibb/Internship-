from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('interns/', views.interns, name='interns'),
    path('interns/<int:id>/', views.processApplication, name='processApplication'),
    path('company/', views.company, name='company'),
]