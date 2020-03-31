from django.urls import path
from .views import *

app_name = 'accounts'
urlpatterns = [
    path('signup/',SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile')
]