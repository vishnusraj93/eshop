from . models import Cart, CartItem
from . views import cartid

def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=cartid(request))
            car_items = CartItem.objects.all().filter(cart=cart[:1])
            for cat_item in car_items:
                item_count += cat_item.qty
        except Cart.DoesNotExist:
            item_count = 0
    return dict(item_count=item_count)