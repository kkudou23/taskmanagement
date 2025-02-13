from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListTaskView.as_view(), name='list-task'),
    path('task/', views.ListTaskView.as_view(), name='list-task'),
    path('task/create/', views.CreateTaskView.as_view(), name='create-task'),
    path('task/<int:pk>/detail', views.DetailTaskView.as_view(), name='detail-task'),
    path('task/<int:pk>/delete/', views.DeleteTaskView.as_view(), name='delete-task'),
    path('task/<int:pk>/update/', views.UpdateTaskView.as_view(), name='update-task'),
]