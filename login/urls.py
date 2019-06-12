from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index')
    # Second parameter (views.index) means it is going to run the views.py from views
];
