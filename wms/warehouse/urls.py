from django.urls import path
from .views import  get_categories,get_warehouses,get_users,create_category,create_user,create_warehouse,update_warehouse,update_category,update_user,delete_user,delete_warehouse, get_warehouse,get_category


urlpatterns = [
    path('create/user/', create_user, name='create_user'),
    path('user/', get_users, name = 'get_user'),
    path('create/category/', create_category,name = 'create_category'),
    path('category/', get_categories, name = 'get_category'),
    path('create/warehouse/', create_warehouse,name = 'create_warehouse'),
    path('warehouse/', get_warehouses, name = 'get_warehouse'),
    path('category/<int:pk>/update', update_category, name='update_category'),  
    path('user/<int:pk>/update', update_user, name='update_user'),
    path('warehouse/<int:pk>/update', update_warehouse, name='update_warehouse'),
    path('user/<int:pk>/delete/', delete_user, name='delete_user'),
    path('warehouse/<int:pk>/', get_warehouse, name='get_warehouse'),
    path('category/<int:pk>/', get_category, name='get_category'),
    path('warehouse/<int:pk>/delete/', delete_warehouse, name='delete_warehouse'),
    ]