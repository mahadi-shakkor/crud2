from django.urls import path
from . import views

urlpatterns = [
    path('signup2/',views.signup2,name="signup2"),
    path('dashboard2/',views.dashboard2,name="dashboard2"),
    path('', views.user_signup_form, name='user_signup_form'),
]
