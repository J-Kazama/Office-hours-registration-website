from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]


# Second parameter (views.index) means it is going to run the views.py from views
