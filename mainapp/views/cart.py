from django.shortcuts import render
from django.views import View
from mainapp.models.product import Products


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Products.get_products_by_id(ids)
        return render(request, 'cart.html', {'products': products})
