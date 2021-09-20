from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Game

# Create your views here.
def all_games(request):
    """A view to show all games"""

    games = Game.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            games = games.filter(queries)

    context = {
        'games': games,
        'search_term': query,
    }

    return render(request, "games/games.html", context)


def game_detail(request, game_id):
    """ A view to show a game's details """

    game = get_object_or_404(Game, pk=game_id)

    context = {
        'game': game,
    }

    return render(request, 'games/game-detail.html', context)
