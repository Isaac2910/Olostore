
from django.contrib import admin
from .models import Product
from django.utils.html import format_html

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'product_type', 'image_display')
    list_filter = ('product_type',)
    search_fields = ('name', 'description')
    list_editable = ('price', 'stock', 'product_type')
    
    def image_display(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.image.url)
        return "Pas d'image"
    image_display.short_description = "Image"

admin.site.register(Product, ProductAdmin)


