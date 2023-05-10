from django.urls import path
from task_manager.tasks.views import TasksIndexView, TaskCreateView, \
    TaskDetailView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', TasksIndexView.as_view(), name='tasks_index'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_show'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    ]
