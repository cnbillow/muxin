from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('dataset/', views.DataSetView.as_view()),
    path('dataset/<int:pk>/', views.DataSetView.as_view()),    
]

urlpatterns = format_suffix_patterns(urlpatterns)