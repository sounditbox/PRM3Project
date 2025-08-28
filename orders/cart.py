from products.models import Product


class Cart:
    SESSION_KEY = 'cart'
    cart: dict[int, dict[str, int | float]]

    # { product_id: {'quantity': 1, 'price': 10.00} }

    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get(self.SESSION_KEY, {})
        print(self.cart)
        self.__session_modified()

    def add(self, product_id: int):
        product = Product.objects.get(id=product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        self.change_quantity(product_id, 1)

    def subtract(self, product_id: int):
        self.change_quantity(product_id, -1)

    def remove(self, product_id: int):
        self.set_quantity(product_id, 0)

    def change_quantity(self, product_id: int, to_add: int):
        if product_id not in self.cart:
            self.set_quantity(product_id, to_add)
        old_quantity = self.cart[product_id]['quantity']
        self.set_quantity(product_id, old_quantity + to_add)

    def set_quantity(self, product_id: int, quantity: int):
        if product_id not in self.cart:
            self.add(product_id)
        if quantity <= 0:
            del self.cart[product_id]
        self.cart[product_id]['quantity'] = quantity
        self.__session_modified()

    def clear(self):
        self.session.pop(self.SESSION_KEY)
        self.__session_modified()

    def __iter__(self):
        for product_id, product_data in self.cart.items():
            product = Product.objects.get(id=product_id)
            yield {
                product_id: {
                    'product': product,
                    'data': product_data,
                    'total_price': product_data['quantity'] * product_data[
                        'price']
                }}

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(
            item['quantity'] * float(item['price']) for item in self.cart.values()
        )

    def __session_modified(self):
        self.session[self.SESSION_KEY] = self.cart
        self.session.modified = True
        print(self.session[self.SESSION_KEY])
