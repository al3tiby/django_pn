from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='Project_list'),
    path('project/create', views.ProjectCreateView.as_view(), name='Project_create'),
    path('project/edit/<int:pk>', views.ProjectUpdateView.as_view(), name='Project_update')
]
