from django.conf.urls import path
from .views import employeeApi

urlpatterns = [
    path('operations/', employeeApi)
]
