from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.LoginOrRegisterView.as_view(), name='login'),
    path('logout/', views.logout, name='logout')
]