from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('user/', views.userPage, name="user-page"),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register, name='register'),
    path('customer/<str:pk>', views.customer, name='customer'),
    path('createOrder/<str:id>', views.createOrder, name='createOrder'),
    path('createCustomer', views.createCustomer, name='createCustomer'),
    path('updateOrder/<str:id>', views.updateOrder, name='updateOrder'),
    path('deleteOrder/<str:id>', views.deleteOrder, name='deleteOrder'),
]