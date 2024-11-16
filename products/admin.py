from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'serie_number', 'quantity')
    search_fields = ('title',)


admin.site.register(Product, ProductAdmin)
