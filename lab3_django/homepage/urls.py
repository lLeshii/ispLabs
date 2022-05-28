from django.urls import path, include
from . import views
from homepage.views import LoginUserView, RegisterUserView, LogoutUserView

urlpatterns = [
    path("", views.HomePageView.as_view(), name='homepage'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('', include('drug_store.urls')),
    path("", include('cart.urls')),
]
