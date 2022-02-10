from django.urls import path
from . import views

app_name = 'shoppingcart'
urlpatterns = [
    path('', views.allprodcat, name='AllProdCat'),
    path('<slug:c_slug>/', views.allprodcat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodetail, name='procatdet')
]
