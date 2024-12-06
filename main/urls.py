from django.urls import path
from . import views

urlpatterns = [
    path('', views.role_selection, name='role_selection'),  # Set role_selection as the default view
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('index/', views.index, name='index'),  # Home page URL pattern
    path('cart/', views.cart_detail, name='cart_detail'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('genre/<str:genre>/', views.genre_products, name='genre_products'),
    path('remove_product/<int:product_id>/', views.remove_product, name='remove_product'),
    path('get_to_know_us/', views.get_to_know_us, name='get_to_know_us'),
    path('success/', views.payment_success, name='payment_success'),
    path('cancel/', views.payment_cancel, name='payment_cancel'),
    path('search/', views.search, name='search'),
    path('role_selection/', views.role_selection, name='role_selection'),
    path('buyer_signup/', views.buyer_signup, name='buyer_signup'),
    path('seller_signup/', views.seller_signup, name='seller_signup'),
    
]