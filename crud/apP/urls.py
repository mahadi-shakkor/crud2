from django.urls import path
from . import views

urlpatterns = [
    path('monitir_realtime_tem_humidity/',views.monitir_realtime_tem_humidity,name='monitir_realtime_tem_humidity'),
     path('add_harvest_info/',views.add_harvest_info,name='add_harvest_info'),
    path('add_batch_to_invantory/',views.add_batch_to_invantory,name='add_batch_to_invantory'),
    path('signup2/',views.signup2,name="signup2"),
    path('dashboard2/',views.dashboard2,name="dashboard2"),
    path('', views.user_signup_form, name='user_signup_form'),
    path('PDemand/', views.PDemandf, name='PDemand'),
    path('user_search/', views.user_search, name='user_search'),
     path('harvest_fields/search/', views.harvest_fields_search, name='harvest_fields_search'),
    path('harvest_fields/create/', views.create_harvest_field, name='create_harvest_field'),
    
]
