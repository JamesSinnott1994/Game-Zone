from django.shortcuts import render, HttpResponse
from .models import Game

# Create your views here.
def all_games(request):
    """A view to show all games"""

    games = Game.objects.all()

    context = {
        'games': games,
    }

    return render(request, "games/games.html", context)
