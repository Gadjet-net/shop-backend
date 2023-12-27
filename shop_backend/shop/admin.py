from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ['title']
    search_fields = ['title']


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ['title']
    search_fields = ['title']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ['title']
    search_fields = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'category',
        'subcategory',
        'company',
        'price',
        'discount',
        'in_stock',
        'rating',
    )
    list_filter = ['category', 'subcategory', 'company', 'rating']
    search_fields = ['title', 'category', 'subcategory', 'company']


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'login',
        'phone_number',
        'balance',
    )
    list_filter = ['login', 'phone_number']


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'text',
        'rating',
    )
    list_filter = ['title']
