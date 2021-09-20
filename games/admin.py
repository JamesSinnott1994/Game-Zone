from django.contrib import admin
from .models import Game, Category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'genre',
        'description',
        'price',
        'rating',
        'image',
    )

    ordering = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )

admin.site.register(Game, ProductAdmin)
admin.site.register(Category, CategoryAdmin)