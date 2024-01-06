from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('result/list/', views.ResultListView.as_view(), name='result_list')
]