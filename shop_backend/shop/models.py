from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.title}'


class Subcategory(models.Model):
    title = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.title} {self.category}'


class Company(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=64, blank=True)
    description = models.TextField(blank=True)
    image = models.CharField(max_length=256, blank=False, default='')
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, related_name='subcategory', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='company', on_delete=models.CASCADE)
    price = models.IntegerField(blank=True, default=0)
    discount = models.IntegerField(default=0)
    in_stock = models.IntegerField(default=10)
    summ_rating = models.IntegerField(blank=False, default=0)
    count_rating = models.IntegerField(blank=False, default=0)

    def __str__(self):
        return f'{self.title} {self.description} {self.price} {self.discount} {self.in_stock} {self.count_rating} {self.summ_rating}'


class Users(AbstractUser):
    login = models.CharField(max_length=128, blank=True, default='', unique=True)
    username = models.CharField(max_length=128, default='', unique=True)
    phone_number = models.CharField(max_length=32, blank=True)

    REQUIRED_FIELDS = ['phone_number', 'username']
    USERNAME_FIELD = 'login'

    def __str__(self):
        return f'{self.login} {self.username} {self.email} {self.password} {self.phone_number} {self.last_login}'


class Order(models.Model):
    owner = models.ForeignKey(Users, related_name='owner', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='products')
    purchase_amount = models.IntegerField(default=0, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner} {self.products} {self.purchase_amount} {self.date}'


class Comments(models.Model):
    title = models.CharField(max_length=64, blank=False)
    text = models.TextField(blank=False)
    rating = models.IntegerField(default=0, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} {self.text} {self.rating}'
