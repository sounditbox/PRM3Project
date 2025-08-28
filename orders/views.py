from django.shortcuts import redirect
from django.views.generic import TemplateView

from orders.forms import CartAddItemForm


class CartDetail(TemplateView):
    template_name = 'orders/cart_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)


def cart_order_add(request, product_id: int):
    cart = request.session.get('cart', {})
    form = CartAddItemForm(request.POST)
    print('Cart:')
    for item in cart:
        print(item)
    if form.is_valid():
        print(form.cleaned_data)
        cart.set_quantity(product_id, form.cleaned_data['quantity'])
    if request.GET.get('next'):
        return redirect(request.GET.get('next'))
    return redirect('orders:cart_detail')
