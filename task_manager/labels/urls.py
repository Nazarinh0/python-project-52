from django.urls import path

urlpatterns = [
    path('', LabelIndexView.as_view(), name='tasks_index'),
    path('create/', LabelCreateView.as_view(), name='task_create'),
    path('<int:pk>/update/', LabelUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', LabelDeleteView.as_view(), name='task_delete'),
    ]