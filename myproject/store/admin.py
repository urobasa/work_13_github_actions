from django.contrib import admin
from .models import Category, Product
from decimal import Decimal

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('category', 'created_at')
    date_hierarchy = 'created_at'


    @admin.action(description='Увеличить цену на 10 процентов')
    def increase_price_by_10_percent(self, request, queryset):
        for product in queryset:
            product.price = product.price * Decimal('1.1')
            product.save()

    actions = [increase_price_by_10_percent]

