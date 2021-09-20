from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Game

# Create your views here.
def all_games(request):
    """A view to show all games"""

    games = Game.objects.all()

    context = {
        'games': games,
    }

    return render(request, "games/games.html", context)


def game_detail(request, game_id):
    """ A view to show a game's details """

    game = get_object_or_404(Game, pk=game_id)

    context = {
        'game': game,
    }

    return render(request, 'games/game-detail.html', context)
