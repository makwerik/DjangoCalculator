from django.urls import path
from .views import *

urlpatterns = [
    path('', index_html, name='index_html')
]