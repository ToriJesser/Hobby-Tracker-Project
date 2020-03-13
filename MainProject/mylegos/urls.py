from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='mylegos'),
    path('Collection/', views.index, name='listLegos'),               #index of lego sets
    path('AddToCollection/', views.add_set, name='createSet'),
    path('Collection/<int:pk>/Details/', views.details_set, name='setDetails'),
    path('Collection/<int:pk>/Edit/', views.edit_set, name='editSet'),
    path('Collection/<int:pk>/delete/', views.delete, name="delete"),
]