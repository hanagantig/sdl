from django.contrib import admin
from product.models import Product, ProductItem
from django.contrib.admin import SimpleListFilter


class ItemsInline(admin.TabularInline):
    model = ProductItem
    extra = 1

    fields = ('title', 'price', 'is_paid')


class ProductAdmin(admin.ModelAdmin):
    inlines = [ItemsInline]
    list_display = ('number', 'doctor', 'company', 'patient', 'is_paid', 'entered_date', 'finished_date')
    search_fields = ['patient']
    list_filter = ('is_paid', 'entered_date')


admin.site.register(Product, ProductAdmin)
