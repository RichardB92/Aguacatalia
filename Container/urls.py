from django.urls import path
from .views import home, us, coming
urlpatterns = [
    path('', home, name='home'),
    path('us/', us, name='us'),
    path('coming/', coming, name='coming'),
]