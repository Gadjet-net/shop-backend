from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ['title']
    search_fields = ['title']


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
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
        'image',
        'category',
        'subcategory',
        'company',
        'price',
        'discount',
        'in_stock',
    )
    list_filter = ['category', 'subcategory', 'company']
    search_fields = ['title', 'category', 'subcategory', 'company']


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'login',
        'username',
        'phone_number',
        'last_login'
    )
    list_filter = ['login', 'username', 'phone_number']


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'text',
        'rating',
    )
    list_filter = ['title']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'owner',
        'purchase_amount',
    )
    list_filter = ['id', 'owner']
