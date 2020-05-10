from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/detail/', views.detail, name='detail part'),
    #path('<part_number>/add/', views.add_part, name='add part'),
]