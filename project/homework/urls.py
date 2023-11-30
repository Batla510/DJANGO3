from django.urls import path,include
from .views import *

urlpatterns = [
    path('',index, name='index'),
    path('about',about, name='about'),
    path('contacts',contacts, name='contacts'),
    path('form',form, name='form'),
]