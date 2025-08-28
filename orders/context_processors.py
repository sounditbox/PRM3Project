from orders.cart import Cart


def cart(request):
    print(request.session.get('cart', {}))
    return {'cart': Cart(request)}
