from django.urls import path
from . import views

urlpatterns = [
    path('', views.entry_list, name='entry_list'),
    path('single-entry/<str:pk>/', views.single_entry, name='single_entry'),
]