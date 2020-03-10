from django.urls import path

from .import views


urlpatterns = [
    path('tasks', views.TaskView.as_view(), name='tasks'),
    path('tasks/create', views.TaskCreate.as_view(), name='task-create'),
    path('tasks/<int:pk>', views.TaskRetrieve.as_view(), name='task-detail')
]