from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.cartdetail, name='cartdetail'),
    path('add/<int:product_id>/', views.addcart, name='addcart'),
    path('remove/<int:product_id>/', views.cart_remove, name='cartremove'),
    path('full_remove/<int:product_id>/', views.full_remove, name='fullremove')
]