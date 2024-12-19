from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import HarvestFieldsViewSet

# Create a router and register our HarvestFields ViewSet
router = DefaultRouter()
router.register(r'api/harvestfields', HarvestFieldsViewSet, basename='harvestfields')

urlpatterns = [
    # Your existing URL patterns
    path('farmer_req_visit_cutomer/', views.farmer_req_visit_cutomer, name='farmer_req_visit_cutomer'),
    path('product_batch_buy/', views.product_batch_buy, name='product_batch_buy'),
    path('wirehouse_manager_connect_Batch_and_sensor/', views.wirehouse_manager_connect_Batch_and_sensor, name='wirehouse_manager_connect_Batch_and_sensor'),
    path('monitir_realtime_tem_humidity/', views.monitir_realtime_tem_humidity, name='monitir_realtime_tem_humidity'),
    path('add_harvest_info/', views.add_harvest_info, name='add_harvest_info'),
    path('add_batch_to_invantory/', views.add_batch_to_invantory, name='add_batch_to_invantory'),
    path('signup2/', views.signup2, name="signup2"),
    path('dashboard2/', views.dashboard2, name="dashboard2"),
    path('', views.user_signup_form, name='user_signup_form'),
    path('PDemand/', views.PDemandf, name='PDemand'),
    path('user_search/', views.user_search, name='user_search'),
    path('harvest_fields/', views.harvest_fields_list, name='harvest_fields_list'),
    path('harvest_fields/create/', views.create_harvest_field, name='create_harvest_field'),
    path('harvest_fields/update/<int:fields_id>/', views.update_harvest_field, name='update_harvest_field'),
    path('harvest_fields/delete/<int:fields_id>/', views.delete_harvest_field, name='delete_harvest_field'),
    path('buy_batch/<int:b_number>/', views.buy_batch, name='buy_batch'),
    path('visit_Fild/<int:hid>/', views.visit_Fild, name='visit_Fild'),


    # DRF API URL for HarvestFields
    path('', include(router.urls)),  # Include the DRF URLs in the existing URL pattern
    path('index/', views.index),
]
