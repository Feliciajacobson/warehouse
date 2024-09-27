# from django.urls import path
# from views import *

# urlpatterns = [
#     path('create/shipment/', create_shipment,name = 'create_shipment'),
#     path('create/supplier/', create_supplier, name='create_supplier'),
#     path('create/product/', create_product,name = 'create_product'),
#     path('product/<int:pk>/update', update_product, name='update_product'),
#     path('shipment/<int:pk>/update', update_shipment, name='update_shipment'),
#     path('supplier/<int:pk>/update', update_supplier, name='update_supplier'),
#     path('product/<int:pk>/delete', delete_product, name='delete_product'),
#     path('shipment/<int:pk>/delete', delete_product, name='delete_shipment'),
#     path('supplier/<int:pk>/delete', delete_product, name='delete_supplier'),
    
# ]

from django.urls import path
from . import views 

urlpatterns = [
    path('create/shipment/', views.create_shipment, name='create_shipment'),
    path('shipment/', views.get_shipments, name = 'get_shipment'),
    path('create/supplier/', views.create_supplier, name='create_supplier'),
    path('supplier/', views.get_suppliers, name = 'get_supplier'),
    path('create/product/', views.create_product, name='create_product'),
    path('product/', views.get_products, name = 'get_product'),
    path('product/<int:pk>/update', views.update_product, name='update_product'),
    path('create/stock/', views.create_stock, name='create_stock'),
    path('stock/', views.get_stocks, name = 'get_stock'),
    path('stock/<int:pk/', views.get_stock, name='get_stock'),
    path('shipment/<int:pk>/update', views.update_shipment, name='update_shipment'),
    path('supplier/<int:pk>/update', views.update_supplier, name='update_supplier'),
    path('product/<int:pk>/delete', views.delete_product, name='delete_product'),
    path('shipment/<int:pk>/delete', views.delete_product, name='delete_shipment'),
    path('supplier/<int:pk>/delete', views.delete_product, name='delete_supplier'),
]
