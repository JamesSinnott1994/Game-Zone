from django.shortcuts import render, redirect, reverse, HttpResponse, get_list_or_404, get_object_or_404
from .models import Game, UserProfile, Wishlist, WishlistItem
from django.contrib import messages


def wishlist(request):
    return render(request, 'wishlist/wishlist.html')


def add_to_wishlist(request, game_id):
    redirect_url = request.POST.get('redirect_url')

    user = get_object_or_404(UserProfile, user=request.user)
    print(user)

    wishlist = Wishlist.objects.get_or_create(user=user)
    wishlist_user = wishlist[0]

    game = Game.objects.get(pk=game_id)

    if request.POST:
        test = WishlistItem.objects.filter(wishlist=wishlist_user, game=game).exists()
        if test:
            messages.error(request, "Product already in your wishlist")
            return redirect(redirect_url)

        else:
            added_item = WishlistItem(wishlist=wishlist_user, game=game)
            added_item.save()
            messages.success(request, "Game added to your wishlist")
            return redirect(redirect_url)
    else:
        messages.error(request, "Click 'Add to wishlist' to add a item ")
        return render(request, 'home/index.html')
