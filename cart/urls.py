from django.urls import path

from cart.views import ProductList

urlpatterns = [
    path("products/", ProductList.as_view(), name="product_list")
]
