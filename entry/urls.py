from django.urls import path
from . import views

urlpatterns = [
    path('', views.entry_list, name='entry_list'),
    path('single-entry/<str:pk>/', views.single_entry, name='single_entry'),
    path('create-entry/', views.create_entry, name='create_entry'),
    path('update-entry/<str:pk>/', views.update_entry, name='update_entry'),
    path('delete-entry/<str:pk>', views.delete_entry, name='delete_entry'),
]