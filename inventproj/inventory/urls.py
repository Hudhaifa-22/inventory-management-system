from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', views.product_create, name='product_create'),
    path('edit/<int:pk>/', views.product_update, name='product_update'),
    path('delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('register/', views.register_view, name='register'),

    path('login/', CustomLoginView.as_view(), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    ]
