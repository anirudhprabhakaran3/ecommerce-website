from django.urls import path
from marketplace import views

urlpatterns = [
    path("", views.home, name='home'),
    path("product/<int:product_id>", views.product, name="view_product"),
    path("cart", views.view_cart, name="view_cart"),
    path("cart/remove/<int:cart_item_id>", views.remove_from_cart, name="remove_from_cart"),
    path("checkout", views.checkout, name='checkout'),
    path("order/<int:order_id>", views.view_order, name="view_order"),
    path("orders", views.list_orders, name='list_orders')
]