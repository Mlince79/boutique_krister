from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HU7R2Gbo34icFevY9rwR3hOkRRa57ZUgnujmitzVeYZ6W2yKVDmCgHlnJ7nmoxF8rba4OZjYn940manDSz8pAPv00pAtCKsOg',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)