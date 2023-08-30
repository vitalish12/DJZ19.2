from django.contrib import admin

from main.models import Product, Category, Version

# Register your models here.
# admin.site.register(Product)
# admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_prod', 'price_prod', 'category')
    list_filter = ('category',)
    search_fields = ('name_prod', 'description_prod')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'version_name', 'is_current')
