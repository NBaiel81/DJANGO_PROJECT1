from django.urls import path
from .views import *  # homepage,us,cont,register,user_list,order

urlpatterns = [
    path('blog/',blog),
    path('post/',post)
    ]
