from django.urls import path
from django.views.decorators.http import require_POST

from . import views
from drug_store.views import OrderCreationView, CreateNewProduct, UpdtaeProduct, DeleteProduct, CreateNewCategory

urlpatterns = [
    path("goods/", views.ProductListView.as_view(), name='product_list'),
    path("categories/", views.CategoryListView.as_view(), name='categories'),
    path("categories/<int:pk>/", views.CategoryDetailView.as_view(), name='concrete_category'),
    path("goods/<int:pk>/", views.ProductDetailView.as_view(), name='product_detail'),
    path('goods/<int:pk>/add/', require_POST(OrderCreationView.as_view()), name='cart_add'),
    path('goods/create/', CreateNewProduct.as_view(), name='create_product'),
    path('goods/create_ct/', CreateNewCategory.as_view(), name='create_category'),
    path('goods/<int:pk>/update/', UpdtaeProduct.as_view(), name='update_product'),
    path('goods/<int:pk>/delete/', DeleteProduct.as_view(), name='delete_product')
]
