from django.urls import path
from . import views

urlpatterns = [
    path("goods/", views.ProductListView.as_view(), name='product_list'),
    path("categories/", views.CategoryListView.as_view(), name='categories'),
    path("categories/<int:pk>/", views.CategoryDetailView.as_view(), name='concrete_category'),
    path("goods/<int:pk>/", views.ProductDetailView.as_view(), name='product_detail'),
]
