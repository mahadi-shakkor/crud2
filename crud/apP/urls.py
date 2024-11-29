from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_signup_form, name='user_signup_form'),
]
