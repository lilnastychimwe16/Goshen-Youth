from django.contrib import admin
from django.urls import include, path
from . import views  # Import views directly if needed
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='youth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.index, name='index'),
    path('add_financial_update/', views.add_financial_update, name='add_financial_update'),
    path('add_notification/', views.add_notification, name='add_notification'),
]

    
