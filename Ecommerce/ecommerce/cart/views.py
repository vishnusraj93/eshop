from django.shortcuts import render, redirect, get_object_or_404
from shoppingcart.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def cartid(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def addcart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=cartid(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=cartid(request))
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.qty < cart_item.product.stock:
            cart_item.qty += 1
            cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, qty=1, cart=cart)
        cart_item.save()
    return redirect('cart:cartdetail')


def cartdetail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=cartid(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cartitem in cart_items:
            total += (cartitem.product.price * cartitem.qty)
            counter += cartitem.qty
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter))


def cart_remove(request, product_id):
    cart = Cart.objects.get(cart_id=cartid(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.qty > 1:
        cart_item.qty -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cartdetail')

def full_remove(request, product_id):
    cart = Cart.objects.get(cart_id=cartid(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart:cartdetail')