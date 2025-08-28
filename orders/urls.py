from django.urls import path

from orders.views import cart_order_add, CartDetail

app_name = 'orders'

urlpatterns = [
    path('cart/add/<int:product_id>/', cart_order_add, name='cart_add'),
    path('cart/', CartDetail.as_view(), name='cart_detail')
]
