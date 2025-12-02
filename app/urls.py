from django.urls import path
from .views import lesson_detail, home

urlpatterns = [
    path('', home, name='home'),
    path('lesson/<int:pk>/', lesson_detail, name='lesson_detail'),
]
