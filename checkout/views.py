from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('games'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JMuYtKGLMUHtvCLMfvpbr9GiPoX3xNDYEbWJrJXY3rAlxyJKJQDMBMjX5RJ5ecw9iWrUlBOcrxZS1JOQayECbfP00edz2rnj0',
        'client_secret': 'test',
    }

    return render(request, template, context)
