from django.shortcuts import render, redirect, reverse, HttpResponse, get_list_or_404, get_object_or_404
from .models import Game, UserProfile, Wishlist, WishlistItem
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def wishlist(request):
    """Shows all games in the user's wishlist"""
    user = get_object_or_404(UserProfile, user=request.user)

    wishlist = Wishlist.objects.get_or_create(user=user)
    wishlist_user = wishlist[0]

    wishlist_exists = WishlistItem.objects.filter(wishlist=wishlist_user).exists()

    games = []
    if wishlist_exists:
        user_wishlist = get_list_or_404(WishlistItem, wishlist=wishlist_user)
        for obj in user_wishlist:
            game = get_object_or_404(Game, name=obj)
            games.append(game)
        context = {
            'wishlist': True,
            'games': games
        }
        return render(request, 'wishlist/wishlist.html', context)

    else:
        context = {
            'wishlist': False,
        }
        return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, game_id):
    """Adds game to the wishlist"""
    redirect_url = request.POST.get('redirect_url')

    user = get_object_or_404(UserProfile, user=request.user)

    wishlist = Wishlist.objects.get_or_create(user=user)
    wishlist_user = wishlist[0]

    game = Game.objects.get(pk=game_id)

    if request.POST:
        game_in_wishlist = WishlistItem.objects.filter(wishlist=wishlist_user, game=game).exists()
        if game_in_wishlist:
            messages.error(request, "Game already in your wishlist")
            return redirect(redirect_url)

        else:
            added_item = WishlistItem(wishlist=wishlist_user, game=game)
            added_item.save()
            messages.success(request, "Game added to your wishlist")
            return redirect(redirect_url)
    else:
        messages.error(request, "Click 'Add to wishlist' to add a item ")
        return render(request, 'home/index.html')

@login_required
def delete_from_wishlist(request, game_id):
    """Removes game from the wishlist"""
    redirect_url = request.POST.get('redirect_url')

    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.get_or_create(user=user)
    wishlist_user = wishlist[0]

    if request.POST:
        game = Game.objects.get(pk=game_id)

        game_in_wishlist = WishlistItem.objects.filter(game=game).exists()

        if game_in_wishlist:
            game = WishlistItem.objects.get(game=game)
            game.delete()
            messages.success(request, "Game removed from wishlist")
            return redirect(redirect_url)

        if game_in_wishlist is None:
            messages.error(request, "Can't delete item as it is not in your wishlist")
            return redirect(redirect_url)
    else:
        messages.error(request, 'Item can only be deleted from your wishlist')
        return render(request, 'home/index.html')
