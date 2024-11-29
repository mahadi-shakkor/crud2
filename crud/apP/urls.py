from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_siunup_form, name='user_siunup_form'),
]
