from django.urls import path
from django.views.decorators.http import require_POST

from . import views
from drug_store.views import OrderCreationView

urlpatterns = [
    path("goods/", views.ProductListView.as_view(), name='product_list'),
    path("categories/", views.CategoryListView.as_view(), name='categories'),
    path("categories/<int:pk>/", views.CategoryDetailView.as_view(), name='concrete_category'),
    path("goods/<int:pk>/", views.ProductDetailView.as_view(), name='product_detail'),
    path('goods/<int:pk>/add/', require_POST(OrderCreationView.as_view()), name='cart_add'),
]
