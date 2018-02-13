from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.list_products, name='list_products'),
    path('new/', views.create_product, name='create_product'),
    path('details/<int:product_id>', views.details, name='details'),
    path('update/<int:product_id>/', views.update_product, name='update_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
