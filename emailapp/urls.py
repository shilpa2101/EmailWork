from django.urls import path
from .views import *
urlpatterns=[
    path('admins/',admins),
    path('contactus/',contact),
    path('contactussucces',contactus_view)
]