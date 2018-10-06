from django.urls import path
from client_portal.views import *

urlpatterns = [
    path('<slug:slug>', patient_information)
]