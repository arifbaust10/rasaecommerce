from django.urls import path
from .views import AddToCart,CartItems,AddCoupon


urlpatterns = [
    path('cart/', CartItems.as_view(), name='cart'),
    path('add_to_cart/<int:product_id>/', AddToCart.as_view(), name='add_to_cart'),
    path('add_coupon/', AddCoupon.as_view(), name='add_coupon'),

]
 