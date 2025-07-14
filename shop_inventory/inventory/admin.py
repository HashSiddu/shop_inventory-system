from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category', 'stock_status')
    list_filter  = ('category',)
    search_fields = ('name',)