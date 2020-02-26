from django.urls import path
from .views import *

urlpatterns = [
    path('post/', post, name='post'),
    path('delete/', delete, name='delete'),
    path('edit/', edit, name='edit'),
    path('update/', update, name='update')
]