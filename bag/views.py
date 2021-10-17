from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from games.models import Game

# Create your views here.


@login_required
def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


@login_required
def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    game = get_object_or_404(Game, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request, f'Updated {game.name} quantity to {bag[item_id]}'
        )
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {game.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


@login_required
def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    game = get_object_or_404(Game, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f'Updated {game.name} quantity to {bag[item_id]}'
        )
    else:
        bag.pop(item_id)
        messages.success(
            request, f'Removed {game.name} from your bag'
        )

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


@login_required
def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        game = get_object_or_404(Game, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed {game.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
