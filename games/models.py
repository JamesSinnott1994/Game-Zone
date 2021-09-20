from django.db import models

# Create your models here.
class Category(models.Model):
    # Fields that correspond to "categories.json" file
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    # Takes in the category model itself
    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Game(models.Model):
    # Foreign key to the category model
    # We'll allow this to be null in the database and blank in forms
    # and if a category is deleted we'll set any products that use it to have null for this field
    # rather than deleting the product.
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    genre = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    
