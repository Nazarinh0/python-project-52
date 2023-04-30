from django.urls import path
from .views import StatusesIndexView, StatusCreateView, StatusDeleteView, StatusUpdateView


urlpatterns = [
    path('', StatusesIndexView.as_view(), name='statuses_index'),
    path('create/', StatusCreateView.as_view(), name='status_create'),
    path('<int:pk>/update/', StatusUpdateView.as_view(), name='status_update'),
    path('<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),
]