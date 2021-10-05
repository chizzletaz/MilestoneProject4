from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    if isinstance(quantity, int):
        total = price * quantity
    else:
        total = price * quantity['quantity']
    return total