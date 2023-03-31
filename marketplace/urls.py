from django.urls import path
from marketplace import views

urlpatterns = [
    path("", views.home, name='home'),
    path("product/<int:product_id>", views.product, name="view_product"),
]