from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.get_orders, name = 'get_order'),
    path('order/create/', views.create_order,name = 'create_order'),
    path('order/<int:pk>/update', views.update_order, name='update_order'),
    path('order/<int:pk>/delete', views.delete_order, name='delete_order'),

    path('create/inventory_movement/', views.create_inventory_movement,name = 'create_inventory_movement'),
    path('inventory_movement/<int:pk>/update', views.update_inventory_movement, name='update_inventory_movement'),
    path('inventory_movement/',views.get_inventory_movements, name ='get_inventory_movement'),
    path('inventory_movement/<int:pk>/', views.get_inventory_movement, name = 'get_inventory_movement'),
    path('inventory_movement/<int:pk>/delete', views.delete_inventory_movement, name='delete_product'),

    
]