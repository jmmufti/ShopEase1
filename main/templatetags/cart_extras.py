# shopease/main/templatetags/cart_extras.py

from django import template

register = template.Library()

@register.filter
def mul(value, arg):
    return value * arg

@register.filter
def total_cart_price(cart_items):
    return sum(item.product.price * item.quantity for item in cart_items)