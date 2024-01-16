from django.urls import path
from .views import LabelsIndexView, LabelCreateView, \
    LabelUpdateView, LabelDeleteView


urlpatterns = [
    path('', LabelsIndexView.as_view(), name='labels_index'),
    path('create/', LabelCreateView.as_view(), name='label_create'),
    path('<int:pk>/update/', LabelUpdateView.as_view(), name='label_update'),
    path('<int:pk>/delete/', LabelDeleteView.as_view(), name='label_delete'),
]
