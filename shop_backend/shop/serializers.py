from rest_framework import serializers

from .models import *


class CategorySerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Subcategory
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Company
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.title')
    subcategory = serializers.ReadOnlyField(source='subcategory.title')
    company = serializers.ReadOnlyField(source='company.title')

    class Meta:
        model = Product
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Users
        fields = [
            'id',
            'login',
            'phone_number',
            'balance',
            'comments'
        ]


class CommentsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.name')

    class Meta:
        model = Comments
        fields = '__all__'
