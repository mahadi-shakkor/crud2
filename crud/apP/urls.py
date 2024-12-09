from django.urls import path
from . import views

urlpatterns = [
    path('monitir_realtime_tem_humidity/',views.monitir_realtime_tem_humidity,name='monitir_realtime_tem_humidity'),
    path('add_batch_to_invantory/',views.add_batch_to_invantory,name='add_batch_to_invantory'),
    path('signup2/',views.signup2,name="signup2"),
    path('dashboard2/',views.dashboard2,name="dashboard2"),
    path('', views.user_signup_form, name='user_signup_form'),
    path('PDemand', views.PDemand, name='PDemand'),
    
]
