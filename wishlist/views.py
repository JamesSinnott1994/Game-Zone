from django.shortcuts import render, redirect, reverse, HttpResponse, get_list_or_404, get_object_or_404
from .models import Game, UserProfile, Wishlist, WishlistItem
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def wishlist(request):
    user = get_object_or_404(UserProfile, user=request.user)
    print(user)

    wishlist = Wishlist.objects.get_or_create(user=user)
    wishlist_user = wishlist[0]

    wishlist_exists = WishlistItem.objects.filter(wishlist=wishlist_user).exists()

    print(wishlist_user)

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
        print("GAME IN WISHLIST")
        return render(request, 'wishlist/wishlist.html', context)

    else:
        context = {
            'wishlist': False,
        }
        print("GAME NOT IN WISHLIST")
        return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, game_id):
    redirect_url = request.POST.get('redirect_url')

    user = get_object_or_404(UserProfile, user=request.user)
    print(user)

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
