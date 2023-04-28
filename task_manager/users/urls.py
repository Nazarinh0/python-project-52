from django.urls import path
from .views import UserCreateView, UserIndexView, UserUpdateView, UserDeleteView


urlpatterns = [
    path('', UserIndexView.as_view(), name='user_index'),
    path('create/', UserCreateView.as_view(), name='sign_up'),
    path('<int:pk>/update', UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete', UserDeleteView.as_view(), name='user_delete'),
]
