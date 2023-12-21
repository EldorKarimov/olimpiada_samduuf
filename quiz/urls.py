from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.QuizDetailView.as_view(), name='quiz_detail'),
    path('<slug:slug>/start/', views.QuizPageView.as_view(), name='quiz_page')
]