from django.db import models
from profiles.models import UserProfile
from games.models import Game


class Wishlist(models.Model):
    """Model that links a game to a user"""
    user = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='wishlist'
    )

    def __str__(self):
        return f'Wishlist ({self.user})'


class WishlistItem(models.Model):
    """A many to many model to save games"""
    wishlist = models.ForeignKey(
        Wishlist, null=False, blank=False,
        on_delete=models.CASCADE,
        related_name='wishlist_items'
    )
    game = models.ForeignKey(
        Game, null=False, blank=False,
        on_delete=models.CASCADE,
        related_name='wishlist_games'
    )

    def __str__(self):
        return self.game.name
