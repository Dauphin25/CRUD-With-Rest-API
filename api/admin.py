from django.contrib import admin
from api.models.category import Category
from api.models.item import Item
from api.models.tags import Tag


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name', 'description')
    fields = ('name', 'description', 'parent_category')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'price', 'stock')
    search_fields = ('name', 'description', 'category', 'price', 'stock')
    list_filter = ('name', 'description', 'category', 'price', 'stock')
    fields = ('name', 'description', 'category', 'tags', 'price', 'stock')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    fields = ('name',)
