from django.urls import path
from seller import views

urlpatterns = [
    path('register', views.register, name='seller_register'),
    path('profile', views.profile, name='seller_profile'),
    path('add_product', views.add_product, name='add_product'),
    path('update_product/<int:id>', views.update_product, name='update_product'),
    path('delete_product/<int:id>', views.delete_product, name='delete_product'),
]