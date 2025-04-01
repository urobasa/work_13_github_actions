from django.urls import path
from .views import (
    home,
    CategoryListView, CategoryDetailView,
    ProductListView, ProductDetailView,
    create_product, edit_product
)

urlpatterns = [
    path('', home, name='home'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', create_product, name='product_create'),
    path('products/<int:pk>/edit/', edit_product, name='product_edit'),
]

