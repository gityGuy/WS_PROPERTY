from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('publish/', views.publish_property, name='publish'),
]
