from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView

from cart.models import Product


class ProductList(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, "product_list.html", {"products": products})


def delete_product(product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
