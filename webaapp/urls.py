from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name='home'),
    
    path('collections',views.collections,name = "collections"),
    path('collections/<str:name>',views.collectionsview,name="collections"),
    path('collections/<str:cname>/<str:pname>',views.product_details,name="product_details"),
    path('BuyNow/<str:name>',views.buynow,name="BuyNow"),
    path('register/',views.register,name="register"),
    path('login/',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('cart',views.cart_page,name="cart"),
    path('addtocart',views.add_to_cart,name="addtocart"),
    path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),
    path('checkout',views.checkout,name='checkout'),
    path('placeholder',views.placeholder,name='placeholder'),
    path('fav',views.fav_page,name="fav"),
    path('favviewpage',views.favviewpage,name="favviewpage"),
    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

