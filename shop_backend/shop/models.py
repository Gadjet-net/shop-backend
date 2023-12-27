from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Subcategory(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Company(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=64, blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, related_name='subcategory', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='company', on_delete=models.CASCADE)
    price = models.IntegerField(blank=True, default=0)
    discount = models.IntegerField(default=0)
    in_stock = models.IntegerField(default=10)
    rating = models.FloatField(blank=True, default=0.0)
    count_rating = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return f'{self.title} {self.description} {self.price} {self.discount} {self.in_stock} {self.rating} {self.count_rating}'


class Users(models.Model):
    name = models.CharField(max_length=64, blank=True)
    login = models.CharField(max_length=32, blank=True)
    phone_number = models.CharField(max_length=128, blank=True)
    password = models.CharField(max_length=32, blank=True)
    balance = models.IntegerField(default=0, blank=True)
    card_number = models.CharField(max_length=19, blank=True)
    card_CVC = models.CharField(max_length=3, blank=True)
    card_date = models.CharField(max_length=16, blank=True)

    def __str__(self):
        return f'{self.name} {self.login} {self.phone_number} {self.password} {self.balance} {self.card_number} {self.card_number} {self.card_CVC} {self.card_date}'


class Comments(models.Model):
    title = models.CharField(max_length=64, blank=False)
    text = models.TextField(blank=False)
    rating = models.IntegerField(default=0, blank=True)
    user = models.ForeignKey(Users, related_name='comments', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.title} {self.text} {self.rating}'


