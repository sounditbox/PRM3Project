from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView

from orders.cart import Cart
# from orders.forms import CartAddItemForm
from products.models import Product


class CartDetail(TemplateView):
    template_name = 'orders/cart_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def cart_order_add(request, product_id: int):
    cart = Cart(request)
    #form = CartAddItemForm(request.POST or None)

    quantity = int(request.POST['quantity'])
    cart.change_quantity(product_id, quantity)
    next_url = request.GET.get('next')
    return redirect(next_url or 'orders:cart_detail')
