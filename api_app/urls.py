from django.urls import path
from .views import (GetAllProductView, get_all_product, GetProductCategoryView,ProductDetail2, ProductDetail,AllProductView, AllProductCreateView, DeleteProduct,
AllProductUpdateView)



urlpatterns = [
    path('products/', GetAllProductView.as_view()),
    path('all-product/', get_all_product),
    path('products/<cat>/', GetProductCategoryView.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()), #for class base view
    path('all-products/', AllProductView.as_view()), #listapi
    path('all_product2/',AllProductCreateView.as_view()),
    path('retrieve_product/<pk>/',ProductDetail2.as_view()),
    path('destroy/<pk>/', DeleteProduct.as_view()),
    path('retrieve-prod/<pk>/', AllProductUpdateView.as_view())

]