from django.urls import path
from . import views

urlpatterns = [
    path('promotions', views.post_list, name='post_list'),
]